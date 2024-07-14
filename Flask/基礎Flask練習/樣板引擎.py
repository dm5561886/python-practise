from flask import Flask  # 載入 Flask
from flask import request  # 載入 Request 物件
from flask import render_template  # 載入 render_template 函式
# 建立 Application 物件, 可以設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder='static',  # 靜態檔案的資料夾名稱
    static_url_path='/'  # 靜態檔案對應的網址路徑
)

# 使用GET方法,處理路徑 "/" 的對應函式


@app.route("/", methods=["GET"])  # 預設GET,可以省略不寫
def index():
    return render_template('index.html', name='小明')


@app.route("/page")
def page():
    return render_template('page.html')


@app.route("/show")
def show():
    name = request.args.get('n', '')
    return "您好 show頁面," + name

# 使用POST方法,處理路徑 "/calculate" 的對應函式


@app.route("/calculate", methods=["POST"])
def calculate():
    # 接收 GET方法的 Query String
    # math_max = request.args.get('max', '')

    math_max = request.form['max']  # 接收 POST 方法的 Query String
    math_max = int(math_max)
    result = 0
    for i in range(1, math_max+1):
        result += i
    return render_template('result.html', data=result)


if __name__ == "__main__":
    app.run(port=3000)
