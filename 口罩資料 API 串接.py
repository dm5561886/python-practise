import requests
import json
# 利用 requests 對 API 來源發送一個請求
url = 'https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json'
response = requests.get(url)

# 將請求回應的內容存成一個字串格式
# response.text

# 將長得像 json 格式的字串解析成字典或列表
data = json.loads(response.text)

med_count = {}
# 填入欄位名稱
for d in data['features']:
    conunty = d['properties']['address'][:3]
    if conunty not in med_count:
        med_count[conunty] = 0
    else:
        med_count[conunty] += 1

print(med_count)
# {'台北市': 123, '新北市': 456 ...}
