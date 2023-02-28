import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.bbc.com/portuguese"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
site = requests.get(URL, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
article = soup.find('h3', class_="bbc-1whbtaf")
headline = article.text
description = article.find_next("p", class_="bbc-1g5xny6").text
tweet = headline+"\n"+description+"\n#tweeter #news #brasil "
#print(tweet)
###############
token = os.getenv('TOKEN_01')
chat_id = os.getenv('TOKEN_02')
msg = (f'{tweet}\nBy GitHub lakeonebr03/ws_news')
url_tel = ("https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&text="+msg)
respost = requests.get(url_tel)
###############
