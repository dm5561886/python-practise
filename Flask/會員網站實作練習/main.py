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
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.member_system

# 初始化 Flask 伺服器
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)


# 設定Session 的密鑰
app.secret_key = "any string but secret"


@app.route("/")  # 首頁
def index():
    return render_template("index.html")


@app.route("/menber")  # 會員頁面
def menber():
    if "name" in session:
        return render_template("menber.html")
    else:
        return redirect("/")


@app.route("/error")  # /errot? msg=錯誤訊息
def error():
    message = request.args.get("msg", "發生錯誤，聯繫客服")
    return render_template("error.html", message=message)


@app.route("/signup", methods=["POST"])
def signup():
    # 從前端接收資料
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    # 根據接收到的資料，和資料庫互動
    collection = db.user

    # 檢查會員集合中是否有相同 email 的文件資料
    result = collection.find_one({
        "email": email
    })
    if result != None:
        return redirect("/error?msg=信箱已經被註冊")
    # 把資料放進資料庫，完成註冊
    collection.insert_one({
        "name": name,
        "email": email,
        "password": password
    })
    return redirect("/")


@app.route("/signin", methods=["POST"])
def signin():
    # 從前端取得使用者輸入
    email = request.form["email"]
    password = request.form["password"]
    # 與資料庫互動
    collection = db.user
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
    # 登入成功，在 Session 紀錄會員資訊，導向到會員頁面
    session["name"] = result["name"]
    return redirect("/menber")


@app.route("/signout")
def signout():
    # 移除 Session 中的會員資訊
    del session["name"]
    return redirect("/")


if __name__ == "__main__":
    # 啟動伺服器在 Port3000
    # debug=True可以重新整理，不用重新啟動
    app.run(port=3000, debug=True)
