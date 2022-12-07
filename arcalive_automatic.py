#@title TEST B
#####1.0.3

!pip install bs4 konlpy matplotlib pandas wordcloud

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

KO_KR=['KO-KR', 'KO-kr', 'Ko-Kr', 'Ko-kr', 'ko-Kr', 'ko-KR', 'ko-kr', 'KR', 'kr', 'Korea', 'Korean', 'korea', 'korean', 'Hangeul', 'hanguel', '한국어', '한글', '한국말', 'gksrnrdj', 'gksrmf', 'gksrnrakf']
EN_GB=['EN-GB', 'EN-gb', 'En-Gb', 'En-gb', 'en-Gb', 'en-GB', 'en-gb', 'EN-US', 'en-us', 'English', 'english', 'ENG', 'eng', 'not american']

version=(f'1.0.4')

class description:
    def first(self):
        if lingua in KO_KR:
            print(f'아카라이브 웹 스크래퍼 {version}입니다.\n주요 채널 목록은 아래와 같습니다.\n')
            print(f'베스트 라이브/live: 45p/month')
            print(f'원신/genshin:  6400p/month\n블루아카이브/bluearchive:  4500p/month\n붕괴3rd/hk3rd:  2400p/month')
            print(f'카운터사이드/counterside:  2000p/month\n던전앤파이터/dunfa:  1800p/month\n명일방주/arknights:  1600p/month')
            print(f'라스트오리진/lastorigin:  900p/month\n벽람항로/azurlane:  750p/month\n프린세스 커넥트 Re:Dive/prcn:  300p/month\n')

        elif lingua in EN_GB:
            print(f'Arcalive Web Scraper {version}.\nHere is the list of major channels as it follows.\n')
            print(f'Best Live/live: 45p/month')
            print(f'Genshin Project/genshin:  6400p/month\nBlue Archive/bluearchive:  4500p/month\nHonkai 3rd/hk3rd:  2400p/month')
            print(f'Counterside/counterside:  2000p/month\nDNF/dunfa:  1800p/month\nArknights/arknights:  1600p/month')
            print(f'Last Origin/lastorigin:  900p/month\nAzur Lane/azurlane:  750p/month\nPrincess Connect Re:Dive/prcn:  300p/month\n')

    def second_normal(self):
        if lingua in KO_KR:
            print(f'\n일반 채널을 선택하셨습니다.\n')

        elif lingua in EN_GB:
            print(f'\nYou have selected a normal channel.\n')
    
    def second_live(self):
        if lingua in KO_KR:
            print(f'\n베스트 라이브 채널을 선택하셨습니다.\n')

        elif lingua in EN_GB:
            print(f'\nYou have selected the Best Live channel.\n')

    def finished(self):
        df.info()
        if lingua in KO_KR:
            print(f'\narcalive_{channel}_page_{n}_{creation_date}.csv의 저장이 완료되었습니다.')
            print(f'아카라이브 {channel} 채널의 최근 {n} 페이지 데이터 수집이 완료되었습니다.\n제작자: EastPersiaLtd\n')

        elif lingua in EN_GB:
            print(f'\nSaving arcalive_{channel}_page_{n}_{creation_date}.csv has completed.')
            print(f'Data collecting of Arcalive {channel} channels latest {n} page(s) has completed.\nCredit: EastPersiaLtd\n')

class desc3:
    def first(self):
        if lingua in KO_KR:
            print(f'NLP-K WordCloud 한국어 스크립트 {version}입니다.\n')
            print(f'NLP-K WordCloud용 스프레드시트 셀렉터를 실행합니다.\n')

        elif lingua in EN_GB:
            print(f'NLP-K WordCloud script {version} for English.\n')
            print(f'Execute spreadsheet selector for NLP-K WordCloud...\n')

    def second(self):
        if lingua in KO_KR:
            print(f'이 파일은 {type1} 형식입니다.\n')

        elif lingua in EN_GB:
            print(f'This file is {type1} format.\n')

    def third(self):
        if lingua in KO_KR:
            print(df.columns,'\n파일의 칼럼 리스트입니다.\n')

        elif lingua in EN_GB:
            print(df.columns,'\nHere is a coloumn list of the file.\n')

    def fourth(self):
        if lingua in KO_KR:
            print(f'준비가 완료되었습니다.\n')

        elif lingua in EN_GB:
            print(f'Preperation has completed.\n')


    def fifth(self):
        if lingua in KO_KR:
            print(f'NLP-K WordCloud 마법사 {version}입니다.\n')
            #####
            print(f'사용할 수 있는 컬러맵 종류는 아래와 같습니다.\n')
            #####
            print(f'계절\nspring/summer/autumn/winter\n')
            #####
            print(f'그레디언트\nviridis/plasma/inferno/magma/cividis\nWistia/cool/hot/afmhot/coolwarm')
            print(f'bwr/seismic/Spectral/twilight/twilight_shifted\nocean/gist_earth/gist_stern/terrain')
            print(f'CMRmap/cubehelix/gnuplot/gnuplot2\n')
            #####
            print(f'스펙트럼\nhsv/brg/gist_rainbow/rainbow/jet\nturbo/nipy_spectral/gist_ncar\n')

        elif lingua in EN_GB:
            print(f'NLP-K WordCloud Wizard {version}.\n')
            #####
            print(f'Here is the list of colourmaps as it follows.\n')
            #####
            print(f'Season\nspring/summer/autumn/winter\n')
            #####
            print(f'Gradient\nviridis/plasma/inferno/magma/cividis\nWistia/cool/hot/afmhot/coolwarm')
            print(f'bwr/seismic/Spectral/twilight/twilight_shifted\nocean/gist_earth/gist_stern/terrain')
            print(f'CMRmap/cubehelix/gnuplot/gnuplot2\n')
            #####
            print('Spectrum\nhsv/brg/gist_rainbow/rainbow/jet\nturbo/nipy_spectral/gist_ncar\n')

    def sixth_custom(self):
        if lingua in KO_KR:
            print(f'지정된 경로의 폰트를 사용합니다.')

        elif lingua in EN_GB:
            print(f'Use custom font on the path.')

    def sixth_noncustom(self):
        if lingua in KO_KR:
            print(f'커스텀 폰트를 사용하지 않습니다. 경고: 차트가 깨질 수 있습니다.')

        elif lingua in EN_GB:
            print(f'Not using custom font. WARNING: CHART WILL NOT DISPLAY CLEARLY.')

    def finished(self):
        if lingua in KO_KR:
            print(f'nlp_k_wordcloud_arcalive_{channel}_page_{n}_{creation_date}.png의 저장이 완료되었습니다.')
            print(f'NLP-K WordCloud 생성이 끝났습니다.\n제작자: EastPersiaLtd\n')

        elif lingua in EN_GB:
            print(f'Saving nlp_k_wordcloud_arcalive_{channel}_page_{n}_{creation_date}.png has completed.')
            print(f'Generating a NLP-K WordCloud chart has completed.\nCredit: EastPersiaLtd\n')
#####

#####
desc=description()
desc3=desc3()

#####Select Channel
lingua=str(input(f'사용할 언어를 고르세요/Select the language you want. KO_KR / EN_GB: '))
#####

if lingua in KO_KR:
    print('한국어를 고르셨습니다.\n')
    desc.first()
    channel=str(input(f'채널의 주소를 영문으로 입력하세요; https://arca.live/b/(채널 주소): '))
    n=int(input(f'\n스크래핑할 페이지의 범위를 입력하세요; 최근 n 페이지만큼-> n: '))

elif lingua in EN_GB:
    desc.first()
    print('You chosen english.\n')
    channel=str(input(f'Please input the channel address; https://arca.live/b/(channel address): '))
    n=int(input(f'\nChoose the range of pages you want to scrap; Collect the latest n pages -> n: '))

#####
creation_date=str(time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time())))

#####Clause 1-1: General Channel
if channel!='live':
    desc.second_normal()
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
    desc.second_live()
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
desc.finished()

##########Wordcloud
desc3.first()
#####

desc3.third()
#####

if lingua in KO_KR:
    column1=str(input('Wordcloud로 만들 칼럼을 지정해주세요(따옴표 생략): '))

elif lingua in EN_GB:
    column1=str(input('Select the column for generating a Wordcloud chart(You may ignore the inverted commas): '))
#####

datas=df[column1].to_list()
#####

desc3.fourth()
#####


#####Customisation
desc3.fifth()
#####
#number=int(input('이 글자 수 미만의 단어는 포함되지 않습니다(정수로 입력): '))
#title=str(input('차트의 타이틀을 입력해주세요: '))
if lingua in KO_KR:
    cmap=str(input('차트에 사용될 컬러맵을 골라주세요: '))

elif lingua in EN_GB:
    cmap=str(input('Select a colourmap for the chart: '))
#####
if lingua in KO_KR:
    font_custom=str(input('차트에 사용하고 싶은 폰트의 위치를 입력하세요: \n'))

elif lingua in EN_GB:
    font_custom=str(input('Select the path of custom font for the chart: \n'))

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
plt.savefig(f'nlp_k_wordcloud_arcalive_{channel}_page_{n}_{creation_date}.png')

#####Show the chart
plt.show()

#####Finished 2
desc3.finished()