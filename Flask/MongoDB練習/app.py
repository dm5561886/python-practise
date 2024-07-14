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
db = client.test  # 選擇操作 test 資料庫
collection = db.users  # 選擇操作 user 集合
# 把資料新增集合中
collection.insert_one({
    "name": "澤軒",
    "gender": "男"
})
print('新增成功')
