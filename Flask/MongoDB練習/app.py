import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# 連線到MongoDB雲端資料庫
uri = "mongodb+srv://dm5561886:wan11345@mycluster.bc5z9vd.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
# 把資料放進資料庫中
db = client.website  # 選擇操作 website 資料庫
collection = db.members  # 選擇操作 members 集合
# 把資料新增集合中
collection.insert_one({
    "email": "test@test.com",
    "password": "test"
})
print('新增成功')
