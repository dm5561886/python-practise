from flask import Flask
from flask import request  # 載入 Request 物件
import json
# 建立 Application 物件, 可以設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder='static',  # 靜態檔案的資料夾名稱
    static_url_path='/'  # 靜態檔案對應的網址路徑
)
# 所有在 static 資料夾底下的檔案，都對應到網址路徑 /static /檔案名稱

# 建立路徑 / 對應的處理函式


@app.route("/")  # 建立網站首頁的回應方式
def index():    # 回應網站首頁連線的函式
    lang = request.headers.get("accept-language")
    print('語言偏好', lang)
    if lang.startswith('en'):
        return json.dumps({
            'Hello Flask': 'ok',
            'text': 'Hello world'
        })
    else:
        return json.dumps({
            'status': 'ok',
            'text': '您好，歡迎光臨'
        }, ensure_ascii=False)  # 指示不要用ASCII編碼處理中文
    # print('請求方法', request.method)  # 取得請求方法
    # print('通訊協定', request.scheme)  # 取得通訊協定
    # print('主機名稱', request)  # 取得主機名稱
    # print('路徑', request.path)  # 取得路徑
    # print('完整的網址', request.url)  # 取得完整的網址
    # print('瀏覽器和作業系統', request.headers.get("user-agent"))
    # print('語言偏好', request.headers.get('accept-language'))
    # print('引薦網址', request.headers.get('referrer'))
    # return "Hello Flask"  # 回傳網站首頁的內容

# 建立路徑/data 對應的處理函式


@app.route("/data")
def getData():
    return "Data Here"


@app.route("/user/<username>")
def handleUser(username):
    if username == "澤軒":
        return "你好" + username
    else:
        return "Hello" + username

# 建立路徑 /getSum 對應的處理函式
# 利用要求字串 (Query String) 提供彈性 /gerSum? min=最小數字 max=最大數字


@app.route("/getSum")
def getSum():  # min+(min+1)+(min+2)+....max
    # 接收要求字串中的參數資料
    maxnumbeer = request.args.get('max', 100)
    maxnumbeer = int(maxnumbeer)
    minnumbeer = request.args.get('min', 1)
    minnumbeer = int(minnumbeer)

    # 以下運算 min+(min+1)+(min+2)+...+max 總和的迴圈邏輯
    result = 0
    for i in range(minnumbeer, maxnumbeer+1):
        result += i
    # 把結果回應給前端
    return '結果:' + str(result)


# 啟動網站伺服器，可透過port參數指定埠號
"""
if __name__ == "__main__":檢查中，這樣可以確保程式在直接執行時啟動伺服器，而不是在被作為模組引入時
"""

if __name__ == "__main__":
    app.run(port=3000)
