import sqlite3
import pandas as pd

# 建立 SQLite 資料庫連線
conn = sqlite3.connect('test.db')
# 讀取資料表資料
df = pd.read_sql_query("SELECT * from students", conn)

# 關閉資料庫連線
conn.close()

# 顯示 DataFrame
print(df)
