import os
import requests
import pandas as pd

KEY = os.environ.get('API_KEY')  # сохраняю ключ для подключения

url = ('http://newsapi.org/v2/everything?'  # search everything
       'q=xiaomi&'  # news keyword
       'from=2021-02-17&'  # from date
       'to=2021-03-17&'  # to date
       'domains=lenta.ru&'  # domain for search
       'language=ru&'  # language 
       'sortBy=popularity&'  # sorting
       'pageSize=30&'  # number of pages
       f'apiKey={KEY}')  # api key

response = requests.get(url)
print(response)
xiaomi_news = response.json()
"""with open('xiaomi.json', 'w') as f:
       f.write(str(xiaomi_news))"""

print(sorted(xiaomi_news.keys()))  # посмотреть ключи ответа сервера
print(xiaomi_news['articles'])

######


