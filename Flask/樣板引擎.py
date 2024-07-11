from flask import Flask  # 載入 Flask
from flask import request  # 載入 Request 物件
from flask import render_template  # 載入 render_template 函式
# 建立 Application 物件, 可以設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder='static',  # 靜態檔案的資料夾名稱
    static_url_path='/'  # 靜態檔案對應的網址路徑
)


@app.route("/")  # 建立網站首頁的回應方式
def index():
    return render_template('index.html', name='小明')


@app.route("/page")
def page():
    return render_template('page.html')


if __name__ == "__main__":
    app.run(port=3000)
