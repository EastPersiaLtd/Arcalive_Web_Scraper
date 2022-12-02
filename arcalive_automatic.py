!pip install bs4 collections konlpy matplotlib pandas wordcloud
##########Import Packages
from bs4 import BeautifulSoup
from collections import Counter
from konlpy.tag import Okt
import matplotlib.pyplot as plt
import os
import pandas as pd
import requests
import time
from wordcloud import WordCloud, STOPWORDS
#####
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
if channel!='live':
    print('일반 채널을 선택하셨습니다.')
    for i in range(n):
      url=f'https://arca.live/b/{channel}?p={i+1}'
      #####
      response=requests.get(url)
      soup=BeautifulSoup(response.text, 'html.parser')
      #####
      title=soup.select('span.title')
      author=soup.select('span.user-info')
      #####
      for j in title:
        post_title.append(j.get_text())
      for k in author:
        post_author.append(k.get_text())

elif channel=='live':
    print('베스트 라이브 채널을 선택하셨습니다.\n베스트 라이브 채널은 현재 작성자 수집에 에러가 있습니다.')
    for i in range(n):
      url=f'https://arca.live/b/{channel}?p={i+1}'
      #####
      response=requests.get(url)
      soup=bs(response.text, 'html.parser')
      #####
      title=soup.select('a.title')
      author=soup.select('span.user-info')
      #####
      for j in title:
        post_title.append(j.get_text())
      for k in author:
        post_author.append(k.get_text())

post_list = list(zip(post_title, post_author))
col=['post_title', 'post_author']
df=pd.DataFrame(post_list, columns=col)
df=df.replace(r'\n',  '', regex=True)
df.to_csv(f'arcalive_{channel}_page_{n}_{creation_date}.csv', index=False, encoding="utf-8-sig")
print(f'arcalive_{channel}_page_{n}_{creation_date}.csv의 저장이 완료되었습니다.')
print(f'아카라이브 {channel} 채널의 최근 {n} 페이지 데이터 수집이 완료되었습니다.\n')

##########Wordcloud
print('한국어 NLP WordCloud 스크립트입니다.\n')
print('NLP WordCloud용 스프레드시트 셀렉터를 실행합니다.\n')
#####
print(df.columns,'\n파일의 칼럼 리스트입니다.\n')
#####
column1=str(input('Wordcloud로 만들 칼럼을 지정해주세요(따옴표 생략): '))
datas=df[column1].to_list()
#####
print('준비가 완료되었습니다.\n')
#####
print('NLP WordCloud 마법사입니다.\n')
#####
print('사용할 수 있는 컬러맵 종류는 아래와 같습니다.\n')
print('계절\nspring/summer/autumn/winter\n')
print('그레디언트\nviridis/plasma/inferno/magma/cividis\nWistia/cool/hot/afmhot/coolwarm')
print('bwr/seismic/Spectral/twilight/twilight_shifted\nocean/gist_earth/gist_stern/terrain')
print('CMRmap/cubehelix/gnuplot/gnuplot2\n')
print('스펙트럼\nhsv/brg/gist_rainbow/rainbow/jet\nturbo/nipy_spectral/gist_ncar\n')
#####
#number=int(input('이 글자 수 미만의 단어는 포함되지 않습니다(정수로 입력): '))
#title=str(input('차트의 타이틀을 입력해주세요: '))
cmap=str(input('차트에 사용될 컬러맵을 골라주세요: '))
#####
font_custom=str(input('차트에 사용하고 싶은 폰트의 위치를 입력하세요: \n'))
font_check=bool(font_custom)
#####
if font_check==True:
    print('지정된 경로의 폰트를 사용합니다.')
    #####
    text="".join(map(str, datas))
    okt=Okt()
    nouns=okt.nouns(text)
    words=[n for n in nouns if len(n)>1]
    counting=Counter(words)
    #####
    wc=WordCloud(
        font_path=font_custom,
        width=1600,
        height=900,
        scale=2.0,
        max_font_size=500,
        prefer_horizontal=True,
        colormap=cmap,
        background_color='mintcream',
    )
elif font_check==False:
    print('커스텀 폰트를 사용하지 않습니다. 경고: 차트가 깨질 수 있습니다.')
    #####
    text="".join(map(str, datas))
    okt=Okt()
    nouns=okt.nouns(text)
    words=[n for n in nouns if len(n)>1]
    counting=Counter(words)
    #####
    wc=WordCloud(
        width=1600,
        height=900,
        scale=2.0,
        max_font_size=500,
        prefer_horizontal=True,
        colormap=cmap,
        background_color='mintcream',
    )
#####
gen=wc.generate_from_frequencies(counting)
#####
plt.figure(figsize=(16, 9))
plt.imshow(gen)
#plt.title(title, fontsize=30)
plt.axis('off')
plt.show()
plt.savefig(f'arcalive_{channel}_page_{n}_{creation_date}_wordcloud.png')
#####
print(f'arcalive_{channel}_page_{n}_{creation_date}_wordcloud.png의 저장이 완료되었습니다.')
print('NLP WordCloud 생성이 끝났습니다.\n제작자: EastPersiaLtd\n')