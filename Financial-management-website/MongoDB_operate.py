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
db = client.financial_management_website  # 選擇操作資料庫
collection = db.user_data  # 選擇操作 user_data 集合
# 要更新的文檔的 ObjectId
document_id = ObjectId('66a7643f1ff22b9023437cae')

# 使用 $unset 刪除整個 cash_entries 字段
# result = collection.update_one(
#    {'_id': document_id},
#    {'$unset': {'cash_entries': ''}}
# )

# print(f"Modified {result.modified_count} document(s)")

# 指定要刪除的索引
# index_to_remove = 0  # 這裡設置為 0，你可以根據需要更改

# 步驟 1: 使用 $unset 將指定索引的元素設置為 null
# collection.update_one(
#    {'_id': document_id},
#    {'$unset': {f'cash_entries.{index_to_remove}': 1}}
# )

# 步驟 2: 使用 $pull 刪除所有 null 元素
# result = collection.update_one(
#    {'_id': document_id},
#    {'$pull': {'cash_entries': None}}
# )

# print(f"Modified {result.modified_count} document(s)")

# 尋找陣列中的所有資料:
# 文檔的 ObjectId
document_id = ObjectId('66a7643f1ff22b9023437cae')
u_name = "test"
# 查詢文檔並只返回 cash_entries 字段
result = collection.find_one(
    {"u_name": u_name},
    # 只返回 cash_entries的資料 排除 id 設定1
    {"cash_entries": 1, "_id": 0}
)

cash_entries = result['cash_entries']
data = {'cash_entries': cash_entries}
# taiwanese_dollars = 0
# us_dollars = 0
# for entry in cash_entries:
#    taiwanese_dollars += int(entry['taiwanese_dollars'])
#    us_dollars += int(entry['us_dollars'])
# for i in cash_entries:
#    print(i)

# print(enumerated_cash_entries)
enumerated_cash = list(enumerate(cash_entries))
# print(enumerated_cash)
# for data in enumerated_cash:
# print(data[0])
# print(data[1]['taiwanese_dollars'])

# for data in enumerated_cash:

#    print(data)


# 指定要刪除的索引
index_to_remove = 0  # 這裡設置為 0，你可以根據需要更改

# 步驟 1: 使用 $unset 將指定索引的元素設置為 null
# collection.update_one(
#    {'_id': document_id},
#    {'$unset': {f'stock_entries.{index_to_remove}': 1}}
# )

# 步驟 2: 使用 $pull 刪除所有 null 元素
# result = collection.update_one(
#    {'_id': document_id},
#    {'$pull': {'stock_entries': None}}
# )


# 要查找的 stock_id
stock_id_to_find = "2330"  # 你可以更改這個值來查找不同的 stock_id

# 執行查詢
r = collection.find_one(
    {
        "_id": document_id,
        "stock_entries": {
            "$elemMatch": {"stock_id": stock_id_to_find}
        }
    },
    {
        "stock_entries.$": 1,
        "_id": 0  # 排除 _id 字段
    }
)
for i in r['stock_entries']:
    print(i['stock_id'])
