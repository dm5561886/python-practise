from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3

url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
# 發送請求 → 接收回應
r = requests.get(url)
# 解析
soup = BeautifulSoup(r.text, 'html.parser')
# 找到匯率表格，attrs表示搜尋 tag attribute 屬性
table = soup.find('table', attrs={'title': "牌告匯率"}).find('tbody')
data = []
# 找到每一個row的資料
rows = table.find_all('tr')
for row in rows:
    currency = row.find('div', class_='visible-phone').text.strip()
    buy = row.find('td', attrs={'data-table': '本行現金買入'}).text.strip()
    sell = row.find('td', attrs={'data-table': '本行現金賣出'}).text.strip()
    instant_buy = row.find('td', attrs={'data-table': '本行即期買入'}).text.strip()
    instant_sell = row.find('td', attrs={'data-table': '本行即期賣出'}).text.strip()
    data.append([currency, buy, sell, instant_buy, instant_sell])

df = pd.DataFrame(
    data, columns=['幣別', '現金匯率本行買入', '現金匯率本行賣出', '即期匯率本行買入', '即期匯率本行賣出'])

print(df)
