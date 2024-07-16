import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
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
# 把資料放進資料庫中
db = client.mywebsite  # 選擇操作 mywebsite 資料庫
collection = db.users  # 選擇操作 users 集合
# 把一個資料".insert_one"新增集合中，並取得新增資料的編號
# result_id = collection.insert_one({
# "name": "leo",
# "email": "leo@test.com",
# "password": "leo",
# "level": "2"
# })
# .inserted_id=>取得新增資料的編號
# print(result_id.inserted_id)

# 一次新增多筆資料 ".insert_many"
# result_id = collection.insert_many([{
# "name": "sam",
# "email": "sam@test.com",
# "password": "leo",
# "level": "3"
# }, {
# "name": "amy",
# "email": "amy@test.com",
# "password": "amy",
# "level": "3"
# }])
# print(result_id.inserted_ids)
# print('新增資料成功')

# 取得集合中的第一筆文件資料
# data = collection.find_one()

# 根據 ObjectId 取得文件資料
# data = collection.find_one(ObjectId("6694fe1e494c758980625daa"))
# print(data)

# 取得文件資料中的欄位
# print(data["_id"])
# print(data["email"])

# 一次取得多筆文件資料
# cursor = collection.find()
# for doc in cursor:
# print(doc)

# 更新集合中的一筆文件資料 ".update_one({篩選條件}, {"$set":{更新的資訊}})"
# result = collection.update_one(
# {"email": "sam@test.com"}, {"$set": {"password": "sam"}})

# $unset清除欄位
# result = collection.update_one(
# {"email": "sam@test.com"}, {"$unset": {"description": "Hi, I'm Tse-Xuan"}})

# $inc 加減數字欄位
# result = collection.update_one(
# {"email": "sam@test.com"}, {"$inc": {"level": 0.5}})

# $mul 乘除數字欄位
# result = collection.update_one(
# {"email": "sam@test.com"}, {"$mul": {"level": 0.5}})


# print("符合篩選條件的文件數量", result.matched_count)
# print("實際更新的文件數量", result.modified_count)

# 更新集合中的多筆文件資料 ".update_many({篩選條件}, {"$set":{更新的資訊}})"
result = collection.update_many({"level": 4}, {"$set": {"level": 2}})
print("符合篩選條件的文件數量", result.matched_count)
print("實際更新的文件數量", result.modified_count)
