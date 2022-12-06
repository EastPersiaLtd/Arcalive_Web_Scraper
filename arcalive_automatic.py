#@title TEST B
#####1.0.3

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

#####Create the lists
post_title=[]
post_unique=[]

class desc1:
    def second_normal(self):
        print('일반 채널을 선택하셨습니다.')
    
    def second_best(self):
        print('베스트 라이브 채널을 선택하셨습니다.')

    def finished(self):
        print(f'arcalive_{channel}_page_{n}_{creation_date}.csv의 저장이 완료되었습니다.')
        print(f'아카라이브 {channel} 채널의 최근 {n} 페이지 데이터 수집이 완료되었습니다.\n제작자: EastPersiaLtd\n')
#####

class desc2:
    def second_normal(self):
        print('You have selected a normal channel.')
    
    def second_best(self):
        print('You have selected the Best Live channel.')

    def finished(self):
        print(f'Saving arcalive_{channel}_page_{n}_{creation_date}.csv has completed.')
        print(f'Data collecting of Arcalive {channel} channels latest {n} page(s) has completed.\nCredit: EastPersiaLtd\n')
#####

class desc3:
    def first(self):
        print('한국어 NLP WordCloud 스크립트입니다.\n')
        print('NLP WordCloud용 스프레드시트 셀렉터를 실행합니다.\n')
    
    def second(self):
        print(f'이 파일은 {type1} 형식입니다.\n')

    def third(self):
        print(df.columns,'\n파일의 칼럼 리스트입니다.\n')

    def fourth(self):
        print('준비가 완료되었습니다.\n')

    def fifth(self):
        print('NLP WordCloud 마법사입니다.\n')
        #####
        print('사용할 수 있는 컬러맵 종류는 아래와 같습니다.\n')
        #####
        print('계절\nspring/summer/autumn/winter\n')
        #####
        print('그레디언트\nviridis/plasma/inferno/magma/cividis\nWistia/cool/hot/afmhot/coolwarm')
        print('bwr/seismic/Spectral/twilight/twilight_shifted\nocean/gist_earth/gist_stern/terrain')
        print('CMRmap/cubehelix/gnuplot/gnuplot2\n')
        #####
        print('스펙트럼\nhsv/brg/gist_rainbow/rainbow/jet\nturbo/nipy_spectral/gist_ncar\n')

    def sixth_custom(self):
        print('지정된 경로의 폰트를 사용합니다.')

    def sixth_noncustom(self):
        print('커스텀 폰트를 사용하지 않습니다. 경고: 차트가 깨질 수 있습니다.')

    def finished(self):
        print(f'nlp_wordcloud_arcalive_{channel}_page_{n}_{creation_date}.png의 저장이 완료되었습니다.')
        print('NLP WordCloud 생성이 끝났습니다.\n제작자: EastPersiaLtd\n')
#####

class inputs:
    def __init__(self):
        self.first_ko=print('아카라이브 웹 스크래퍼 1.0.3입니다.\n\n주요 채널 목록은 아래와 같습니다.\n\n원신/genshin:  6400p/month\n블루아카이브/bluearchive:  4500p/month\n붕괴3rd/hk3rd:  2400p/month\n카운터사이드/counterside:  2000p/month\n던전앤파이터/dunfa:  1800p/month\n명일방주/arknights:  1600p/month\n라스트오리진/lastorigin:  900p/month\n벽람항로/azurlane:  750p/month\n프린세스 커넥트 Re:Dive/prcn:  300p/month\n')
        self.channelk0=input('채널의 주소를 영문으로 입력하세요; https://arca.live/b/(채널 주소): ')
        self.nk0=input('크롤링할 페이지의 범위를 입력하세요; 최근 n 페이지만큼-> n: ')
        #####
        self.first_en=0
        self.channele0=0
        self.ne0=0
#####
    
    def first(self):
        self.first_enx=self.first_en
        self.first_kox=self.first_ko

    def channelx1(self):
        self.channelx1=self.channelk0

    def nx1(self):
        self.nx1=self.nk0

    #def printinp(self):
        #print(f'{inputs.channelx1} 채널입니다. {inputs.nx1} 페이지 만큼 찾습니다.')
#####

#####
desc1=desc1()
desc2=desc2()
desc3=desc3()
inputs=inputs()

#####Select Channel
inputs.channelx1()
channel=inputs.channelx1
#####
inputs.nx1()
n=int(inputs.nx1)
#####
creation_date=str(time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time())))

#####Clause 1-1: General Channel
if channel!='live':
    desc1.second_normal()
    for i in range(n):
        url=f'https://arca.live/b/{channel}?p={i+1}'
        #####
        response=requests.get(url)
        soup=BeautifulSoup(response.text, 'html.parser')
        #####
        title=soup.select('span.title')
        #####
        unique_selector=str('div > div.vrow-top > span.vcol.col-id > span')
        unique=soup.select(unique_selector)
        #####
        for j in title:
            post_title.append(j.get_text())
        for k in unique:
            post_unique.append(k.get_text())

#####Clause 1-2: Best Live Channel
elif channel=='live':
    desc1.second_best()
    for i in range(n):
        url=f'https://arca.live/b/{channel}?p={i+1}'
        #####
        response=requests.get(url)
        soup=BeautifulSoup(response.text, 'html.parser')
        #####
        title=soup.select('a.title')
        #####
        for j in title:
            post_title.append(j.get_text())

#####List JOIN
if channel!='live':
    post_list=list(zip(post_title, post_unique))
    col=['post_title', 'post_unique']
elif channel=='live':
    post_list=post_title
    col=['post_title']

#####DataFrame conversion
df=pd.DataFrame(post_list, columns=col)
df=df.replace(r'\n', '', regex=True)
df.to_csv(f'arcalive_{channel}_page_{n}_{creation_date}.csv', index=False, encoding="utf-8-sig")

#####Finished
desc1.finished()

##########Wordcloud
desc3.first()
desc3.third()
#####
column1=str(input('Wordcloud로 만들 칼럼을 지정해주세요(따옴표 생략): '))
datas=df[column1].to_list()
#####
desc3.fourth()

#####Customisation
desc3.fifth()
#####
#number=int(input('이 글자 수 미만의 단어는 포함되지 않습니다(정수로 입력): '))
#title=str(input('차트의 타이틀을 입력해주세요: '))
cmap=str(input('차트에 사용될 컬러맵을 골라주세요: '))
#####
font_custom=str(input('차트에 사용하고 싶은 폰트의 위치를 입력하세요: \n'))
font_check=bool(font_custom)

#####Clause 2-1: Generate the chart w/ custom font
if font_check==True:
    desc3.sixth_custom()
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

#####Clause 2-2: Generate the chart w/o custom font
elif font_check==False:
    desc3.sixth_noncustom()
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

#####Creation
gen=wc.generate_from_frequencies(counting)

#####Showing the chart
plt.figure(figsize=(16, 9))
plt.imshow(gen)
#plt.title(title, fontsize=30)
plt.axis('off')

#####Save the chart
plt.savefig(f'nlp_wordcloud_arcalive_{channel}_page_{n}_{creation_date}.png')

#####Show the chart
plt.show()

#####Finished 2
desc3.finished()