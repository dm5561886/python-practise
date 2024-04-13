import requests
import json
# 利用 requests 對 API 來源發送一個請求
url = 'https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json'
response = requests.get(url)

# 將請求回應的內容存成一個字串格式
# response.text

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

print(med_count)
# {'台北市': 123, '新北市': 456 ...}

# 計算出每個地區的成人剩餘口罩數量，並且將結果從大到小排列
mask_count = {}
for d in data['features']:
    conunty = d['properties']['address'][:3]
    if conunty not in mask_count:
        mask_count[conunty] = 0
    else:
        mask_adult = d['properties']['mask_adult']
        mask_count[conunty] += mask_adult
# 將結果從大到小排列
# dictionary本身不可迭代（不能排序），但可以針對dictionary的key or value or item(both)進行排序
# sorted(mask_count_address.items()後會變成包含tuple的list，所以外面要再包個dict轉回字典
mesk_count = dict(
    sorted(mask_count.items(), reverse=True, key=lambda item: item[1]))

print(mask_count)
