import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
post_title=[]
post_author=[]
#####
channel=str(input('채널의 주소를 영문으로 입력하세요; https://arca.live/b/(채널 주소): '))
n=int(input('크롤링할 페이지의 범위를 입력하세요; 최근 n 페이지만큼-> n:'))
creation_date=str(time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time())))
#####
for i in range(n):
    url=f'https://arca.live/b/{channel}?p={i+1}'
    #####
    response=requests.get(url)
    soup=bs(response.text, 'html.parser')
    #####
    title=soup.select('span.title')
    author=soup.select('span.user-info')
    #time=soup.select('span.vcol.col-time')
    #####
    for j in title:
      post_title.append(j.get_text())
    for k in author:
      post_author.append(k.get_text())

post_list = list(zip(post_title, post_author))
col=['post_title', 'post_author']
df=pd.DataFrame(post_list, columns=col)
df.to_csv(f'arcalive_{channel}_page_{n}_{creation_date}.csv', index=False, encoding="utf-8-sig")