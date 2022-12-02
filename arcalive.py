!pip install bs4 pandas

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
post_title=[]
post_author=[]
#####
print('아카라이브 웹 스크래퍼입니다.\n주요 채널 목록은 아래와 같습니다.\n')
print('원신/genshin:    6400p/month\n블루아카이브/bluearchive:    4500p/month\n붕괴3rd/hk3rd:    2400p/month\n카운터사이드/counterside:    2000p/month')
print('던전앤파이터/dunfa:    1800p/month\n명일방주/arknights:    1600p/month\n라스트오리진/lastorigin:    900p/month\n아즈렌/azurlane:    750p/month')
print('프린세스 커넥트 Re:Dive/prcn:    300p/month\n')
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
    #####
    for j in title:
      post_title.append(j.get_text())
    for k in author:
      post_author.append(k.get_text())

post_list = list(zip(post_title, post_author))
col=['post_title', 'post_author']
df=pd.DataFrame(post_list, columns=col)
df=df.replace(r'\n',  ' ', regex=True)
df.to_csv(f'arcalive_{channel}_page_{n}_{creation_date}.csv', index=False, encoding="utf-8-sig")
print(f'아카라이브 {channel} 채널의 최근 {n} 페이지 데이터 수집이 완료되었습니다.\n다운로드된 파일은 폴더를 열어 확인해주세요.\n제작자: EastPersiaLtd')