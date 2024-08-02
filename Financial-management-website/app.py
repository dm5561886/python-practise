import logging
import matplotlib.pyplot as plt
import os
import pymongo
from flask import Flask, render_template, request, redirect, session
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests
import math
import matplotlib
matplotlib.use('Agg')

# 設置日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 初始化資料庫連線
uri = "mongodb+srv://dm5561886:wan11345@mycluster.bc5z9vd.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster"
client = MongoClient(uri, server_api=ServerApi('1'))

# 檢查與 MongoDB 伺服器的連接是否成功
try:
    client.admin.command('ping')
    logger.info("Successfully connected to MongoDB!")
except Exception as e:
    logger.error(f"MongoDB connection error: {e}")

db = client.financial_management_website

# 初始化 Flask 伺服器
app = Flask(__name__, static_folder="static", static_url_path="/")
app.secret_key = "any string but secret"

# 設置靜態文件夾路徑
base_dir = os.path.abspath(os.path.dirname(__file__))
static_folder = os.path.join(base_dir, 'static')
if not os.path.exists(static_folder):
    os.makedirs(static_folder)


@app.route("/")
def signin_page():
    return render_template("signin.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/signup", methods=["POST"])
def signup():
    # 從前端接收資料
    u_name = request.form["u_name"]
    email = request.form["email"]
    password = request.form["password"]

    # 根據接收到的資料，和資料庫互動
    collection = db.user_data
    result = collection.find_one({"email": email})
    if result is not None:
        return redirect("/error?msg=信箱已被註冊")

    # 把資料放進資料庫，完成註冊
    collection.insert_one({
        "u_name": u_name,
        "email": email,
        "password": password
    })

    return redirect("/")


@app.route("/signin", methods=["POST"])
def signin():
    email = request.form["email"]
    password = request.form["password"]
    collection = db.user_data
    result = collection.find_one({
        "$and": [
            {"email": email},
            {"password": password}
        ]
    })
    if result is None:
        return redirect("/error?msg=帳號或密碼錯誤")
    session["u_name"] = result["u_name"]
    return redirect("/index")


@app.route("/signout")
def signout():
    del session["u_name"]
    return redirect("/")


@app.route("/error")
def error():
    message = request.args.get("msg", "發生錯誤，聯繫客服")
    return render_template("error.html", message=message)


@app.route("/index")
def index():
    if "u_name" not in session:
        return redirect("/")

    u_name = session["u_name"]
    collection = db.user_data
    result = collection.find_one(
        {"u_name": u_name},
        {"cash_entries": 1}
    )
    cash_entries = result.get('cash_entries', [])
    taiwanese_dollars = sum(int(entry['taiwanese_dollars'])
                            for entry in cash_entries)
    us_dollars = sum(int(entry['us_dollars']) for entry in cash_entries)

    # 獲取匯率資訊
    try:
        r = requests.get('https://tw.rter.info/capi.php')
        currency = r.json()
        exchange_rate = currency['USDTWD']['Exrate']
    except Exception as e:
        logger.error(f"Error fetching exchange rate: {e}")
        exchange_rate = 30  # 假設的匯率，如果無法獲取實際匯率

    total = math.floor(taiwanese_dollars + us_dollars * exchange_rate)

    # 獲取股票資訊
    result2 = collection.find_one(
        {"u_name": u_name},
        {"stock_entries": 1}
    )
    stock_entries = result2.get('stock_entries', [])
    unique_stock_list = list(set(data['stock_id'] for data in stock_entries))

    # 計算股票總市值
    total_stock_value = 0
    stock_info = []
    for stock in unique_stock_list:
        result = collection.find_one(
            {
                "u_name": u_name,
                "stock_entries": {
                    "$elemMatch": {"stock_id": stock}
                }
            },
            {
                "stock_entries.$": 1,
                "_id": 0
            }
        )
        stock_entries = result['stock_entries']
        stock_cost = sum(int(d['stock_num']) * int(d['stock_price']) +
                         int(d['processing_fee']) + int(d['tax'])
                         for d in stock_entries)
        shares = sum(int(d['stock_num']) for d in stock_entries)

        # 取得目前股價
        try:
            url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&stockNo={stock}"
            response = requests.get(url)
            data = response.json()
            price_array = data['data']
            current_price = float(price_array[-1][6])
        except Exception as e:
            logger.error(f"Error fetching stock price for {stock}: {e}")
            current_price = 0  # 如果無法獲取股價，設為0

        total_value = int(current_price * shares)
        total_stock_value += total_value
        average_cost = round(stock_cost / shares, 2) if shares else 0
        rate_of_return = round((total_value - stock_cost)
                               * 100 / stock_cost, 2) if stock_cost else 0

        stock_info.append({
            'stock_id': stock,
            'stock_cost': stock_cost,
            'total_value': total_value,
            'average_cost': average_cost,
            'shares': shares,
            'current_price': current_price,
            'rate_of_return': rate_of_return
        })

    for stock in stock_info:
        stock['value_percentage'] = round(
            stock['total_value'] * 100 / total_stock_value, 2) if total_stock_value else 0

    # 繪製股票圓餅圖
    if unique_stock_list:
        labels = tuple(unique_stock_list)
        sizes = [d['total_value'] for d in stock_info]
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.pie(sizes, labels=labels, autopct=None, shadow=None)
        fig.subplots_adjust(top=1, bottom=0, right=1,
                            left=0, hspace=0, wspace=0)
        try:
            plt.savefig(os.path.join(static_folder, "piechart.jpg"), dpi=200)
            logger.info("Stock pie chart saved successfully")
        except Exception as e:
            logger.error(f"Error saving stock pie chart: {e}")
    else:
        try:
            os.remove(os.path.join(static_folder, 'piechart.jpg'))
        except FileNotFoundError:
            pass

    # 繪製股票現金圓餅圖
    if us_dollars != 0 or taiwanese_dollars != 0 or total_stock_value != 0:
        labels = ('USD', 'TWD', 'Stock')
        sizes = (us_dollars * exchange_rate,
                 taiwanese_dollars, total_stock_value)
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.pie(sizes, labels=labels, autopct=None, shadow=None)
        fig.subplots_adjust(top=1, bottom=0, right=1,
                            left=0, hspace=0, wspace=0)
        try:
            plt.savefig(os.path.join(static_folder, "piechart2.jpg"), dpi=200)
            logger.info("Asset allocation pie chart saved successfully")
        except Exception as e:
            logger.error(f"Error saving asset allocation pie chart: {e}")
    else:
        try:
            os.remove(os.path.join(static_folder, 'piechart2.jpg'))
        except FileNotFoundError:
            pass

    data = {
        'show_pic_1': os.path.exists(os.path.join(static_folder, 'piechart.jpg')),
        'show_pic_2': os.path.exists(os.path.join(static_folder, 'piechart2.jpg')),
        'taiwanese_dollars': taiwanese_dollars,
        'us_dollars': us_dollars,
        'currency': exchange_rate,
        'total': total,
        'enumerated_cash': list(enumerate(cash_entries)),
        'stock_info': stock_info
    }

    return render_template("index.html", data=data)


@app.route("/cash")
def cash():
    return render_template("cash.html")


@app.route("/cash", methods=["POST"])
def submit_cash():
    u_name = session["u_name"]
    taiwanese_dollars = request.form["taiwanese-dollars"]
    us_dollars = request.form["us-dollars"]
    note = request.form["note"]
    date = request.form["date"]

    user_collection = db.user_data
    cash_entry = {
        "taiwanese_dollars": taiwanese_dollars,
        "us_dollars": us_dollars,
        "note": note,
        "date": date
    }
    user_collection.update_one(
        {"u_name": u_name},
        {"$push": {"cash_entries": cash_entry}}
    )

    return redirect("/index")


@app.route("/del_cash", methods=["POST"])
def del_cash():
    id = request.values['id']
    u_name = session["u_name"]
    collection = db.user_data
    collection.update_one(
        {'u_name': u_name},
        {'$unset': {f'cash_entries.{id}': 1}}
    )
    collection.update_one(
        {'u_name': u_name},
        {'$pull': {'cash_entries': None}}
    )
    return redirect("/index")


@app.route("/stock")
def stock():
    return render_template("stock.html")


@app.route("/stock", methods=["POST"])
def submit_stock():
    u_name = session["u_name"]
    stock_id = request.form["stock-id"]
    stock_num = request.form["stock-num"]
    stock_price = request.form["stock-price"]
    processing_fee = request.form["processing-fee"]
    tax = request.form["tax"]
    date = request.form["date"]

    user_collection = db.user_data
    stock_entry = {
        "stock_id": stock_id,
        "stock_num": stock_num,
        "stock_price": stock_price,
        "processing_fee": processing_fee,
        "tax": tax,
        "date": date
    }
    user_collection.update_one(
        {"u_name": u_name},
        {"$push": {"stock_entries": stock_entry}}
    )

    return redirect("/index")


if __name__ == "__main__":
    app.run(port=3000, debug=True)
