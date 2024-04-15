import requests
from bs4 import BeautifulSoup


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

print(news)
