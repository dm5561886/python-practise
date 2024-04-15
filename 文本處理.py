import requests
from bs4 import BeautifulSoup
import jieba


# 利用 requests 對 API 來源發送一個請求
response = requests.get('https://udn.com/news/breaknews/1')
soup = BeautifulSoup(response.text)

news = []
for link in soup.find_all('h3', class_='rounded-thumb__title')[:4]:  # 前四篇新聞
    news_url = link.a['href']
    news_response = requests.get('https://udn.com' + news_url)
    news_soup = BeautifulSoup(news_response.text)
    news_content = news_soup.find(
        'div', class_='article-content__paragraph').text.strip().replace('\n', ' ')
    news.append(news_content)


# 精確模式斷詞
# 定義變數名稱
tokens = []
for d in news:
    token = list(jieba.cut(d, HMM=False))  # token = d 字串斷詞結果
    tokens.append(token)

word_count = {}
for word in tokens:
    for counts in word:
        if counts in word_count:
            word_count[counts] += 1
        else:
            word_count[counts] = 1

word_count = dict(
    sorted(word_count.items(), reverse=True, key=lambda item: item[1]))
print(word_count)
