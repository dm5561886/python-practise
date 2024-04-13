import requests
import json
# 利用 requests 對 API 來源發送一個請求
url = 'https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json'
response = requests.get(url)

# 將請求回應的內容存成一個字串格式
d = response.text

# 將長得像 json 格式的字串解析成字典或列表
data = json.loads(d)

print(data)
