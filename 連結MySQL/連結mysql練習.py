import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='dm5561886',
                                     database='sql_tutorial')
cursor = connection.cursor()

# 創建資料庫
# cursor.execute("CREATE DATABASE `qq` ;")

# 取得所有資料庫名稱
# cursor.execute("SHOW DATABASES;")
# records = cursor.fetchall()
# for i in records:
#    print(i)

# 選擇資料庫或在連結資料庫時打上去
# cursor.execute("USE `sql_tutorial`;")

# 取得部門所有資料
cursor.execute("SELECT * FROM `branch`;")
# 取得抓到的資料
records = cursor.fetchall()
for i in records:
    print(i)

cursor.close()
connection.close()
