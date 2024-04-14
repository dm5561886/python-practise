import requests
import json
import sqlite3
import datetime

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS pharmacies
             (city text, counts text, createdAt datetime)''')
c.execute('''DELETE FROM pharmacies''')
conn.commit()

# 利用 requests 對 API 來源發送一個請求
url = 'https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json'
response = requests.get(url)

# 將請求回應的內容存成一個字串格式response.text
# 將長得像 json 格式的字串解析成字典或列表
data = json.loads(response.text)

# 計算各地區的藥局數量
med_count = {}
# 填入欄位名稱
for d in data['features']:
    conunty = d['properties']['address'][:3]
    if conunty not in med_count:
        med_count[conunty] = 0
    else:
        med_count[conunty] += 1

for i in med_count.items():
    city = i[0]
    counts = i[1]
    t = datetime.datetime.now()
    print(f"INSERT INTO stocks VALUES ('{city}', {counts}, '{t}')")
    c.execute(f"INSERT INTO pharmacies VALUES ('{city}', {counts}, '{t}')")
    conn.commit()

# 查詢資料
c.execute("SELECT * FROM pharmacies")
print(c.fetchall())  # 取得所有查詢結果的資料

conn.commit()
conn.close()
