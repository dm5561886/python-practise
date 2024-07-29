import pymongo
from flask import *
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# 初始化資料庫連線
# 連線到MongoDB雲端資料庫
# 建立一個新的客戶端並連接到伺服器
uri = "mongodb+srv://dm5561886:wan11345@mycluster.bc5z9vd.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster"
client = MongoClient(uri, server_api=ServerApi('1'))

# 檢查與 MongoDB 伺服器的連接是否成功(發送 ping 以確認連線成功)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You -successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.financial_management_website

# 初始化 Flask 伺服器
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
app.secret_key = "any string but secret"


@app.route("/")  # 登入頁面
def signin_page():
    return render_template("signin.html")


@app.route("/register")  # 註冊會員
def register():
    return render_template("register.html")


@app.route("/signup", methods=["POST"])  # 接收註冊資料
def signup():
    # 從前端接收資料
    u_name = request.form["u_name"]
    email = request.form["email"]
    password = request.form["password"]
    # 根據接收到的資料，和資料庫互動
    collection = db.user_data
   # 檢查會員集合中是否有相同 email 的文件資料
    result = collection.find_one({
        "email": email
    })
    if result != None:
        return redirect("/error?msg=信箱已被註冊")

    # 把資料放進資料庫，完成註冊
    collection.insert_one({
        "u_name": u_name,
        "email": email,
        "password": password
    })

    return redirect("/")


@app.route("/signin", methods=["POST"])  # 處理登入路由
def signin():
    # 從前端取得使用者輸入
    email = request.form["email"]
    password = request.form["password"]
    # 與資料庫互動
    collection = db.user_data
    # 檢查信箱密碼是否正確
    result = collection.find_one({
        "$and": [
            {"email": email},
            {"password": password}
        ]
    })
    # 找不到對應的資料，登入失敗，導向到錯誤頁面
    if result == None:
        return redirect("/error?msg=帳號或密碼錯誤")
    # 登入成功，導向到會員頁面(理財網站首頁)
    # 在 Session 紀錄會員資訊(這邊使用會員名稱)，導向到會員頁面
    session["u_name"] = result["u_name"]
    return redirect("/index")


@app.route("/signout")  # 登出功能
def signout():
    # 移除 session 中的會員資訊
    del session["u_name"]
    return redirect("/")


@app.route("/error")
# /errot? msg=錯誤訊息
# 帳號登入錯誤頁面
def error():
    message = request.args.get("msg", "發生錯誤，聯繫客服")
    return render_template("error.html", message=message)


@app.route("/index")  # 理財網站頁面
def index():
    # session處理，沒有登入信箱和密碼，無法直接透過網址看到理財網站頁面
    if "u_name" in session:
        return render_template("index.html")
    else:
        return redirect("/")


@app.route("/cash")  # 現金頁面
def cash():
    return render_template("cash.html")


@app.route("/stock")  # 股票頁面
def stock():
    return render_template("stock.html")


if __name__ == "__main__":
    # 啟動伺服器在 Port3000
    # debug=True可以重新整理，不用重新啟動
    app.run(port=3000, debug=True)
