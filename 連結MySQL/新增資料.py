import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='dm5561886',
                                     database='sql_tutorial')
cursor = connection.cursor()

# 新增
# cursor.execute("INSERT INTO `branch` VALUES(5, 'qq', NULL);")
# 修改
# cursor.execute("UPDATE `branch` SET `manager_id`= NULL WHERE `branch_id` = 4;")
# 刪除
cursor.execute("DELETE FROM `branch` WHERE `branch_id`=4;")


cursor.close()
# 確認執行
connection.commit()
connection.close()
