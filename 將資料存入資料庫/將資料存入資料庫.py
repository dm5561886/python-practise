import requests
import json
import sqlite3
import datetime

conn = sqlite3.connect('example.db')
c = conn.cursor()

# 新增且清空資料表
c.execute('''CREATE TABLE IF NOT EXISTS pharmacies
             (city text, counts text, createdAt datetime)''')
c.execute('''DELETE FROM pharmacies''')

c.execute('''CREATE TABLE IF NOT EXISTS masks
             (maskcity text, maskcount text, createdAt datetime)''')
c.execute('''DELETE FROM masks''')
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
    print(f"INSERT INTO pharmacies VALUES ('{city}', {counts}, '{t}')")
    c.execute(f"INSERT INTO pharmacies VALUES ('{city}', {counts}, '{t}')")
    conn.commit()

# 計算出每個地區的成人剩餘口罩數量
mask_count = {}
for d in data['features']:
    conunty = d['properties']['address'][:3]
    if conunty not in mask_count:
        mask_count[conunty] = 0
    else:
        mask_adult = d['properties']['mask_adult']
        mask_count[conunty] += mask_adult

for j in mask_count.items():
    maskcity = j[0]
    maskcount = j[1]
    t2 = datetime.datetime.now()
    c.execute(
        f"INSERT INTO masks VALUES ('{maskcity}', {maskcount}, '{t2}')")
    conn.commit()

# 查詢資料
c.execute("SELECT * FROM pharmacies")
print(c.fetchall())

c.execute("SELECT * FROM masks")
print(c.fetchall())

conn.commit()
conn.close()
