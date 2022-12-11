#@title TEST A

!pip install bs4 pandas

##########Import Packages
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

#####Create the lists
post_title=[]
post_unique=[]

KO_KR=['KO_KR', 'ko_kr', 'KO-KR', 'KO-kr', 'Ko-Kr', 'Ko-kr', 'ko-Kr', 'ko-KR', 'ko-kr', 'KR', 'kr', 'Korea', 'Korean', 'korea', 'korean', 'Hangeul', 'hanguel',
'한국어', '한글', '한국말', 'gksrnrdj', 'gksrmf', 'gksrnrakf']
EN_GB=['EN_GB', 'en_gb', 'EN-GB', 'EN-gb', 'En-Gb', 'En-gb', 'en-Gb', 'en-GB', 'en-gb', 'EN-US', 'en-us', 'English', 'english', 'ENG', 'eng', 'not american']

version=(f'1.0.5')

class description:
    def first(self):
        if lingua in KO_KR:
            print(f'''
한국어를 고르셨습니다.

아카라이브 웹 스크래퍼 {version}입니다.

주요 채널 목록은 아래와 같습니다.

베스트 라이브/live: 45p/month
원신/genshin:  6400p/month
블루아카이브/bluearchive:  4500p/month
붕괴3rd/hk3rd:  2400p/month
카운터사이드/counterside:  2000p/month
던전앤파이터/dunfa:  1800p/month
명일방주/arknights:  1600p/month
라스트오리진/lastorigin:  900p/month
벽람항로/azurlane:  750p/month
프린세스 커넥트 Re:Dive/prcn:  300p/month
''')
        elif lingua in EN_GB:
            print(f'''
You chosen english.

Arcalive Web Scraper {version}.

Here is the list of major channels as it follows.

Best Live/live: 45p/month
Genshin Project/genshin:  6400p/month
Blue Archive/bluearchive:  4500p/month
Honkai 3rd/hk3rd:  2400p/month
Counterside/counterside:  2000p/month
DNF/dunfa:  1800p/month
Arknights/arknights:  1600p/month
Last Origin/lastorigin:  900p/month
Azur Lane/azurlane:  750p/month
Princess Connect Re:Dive/prcn:  300p/month
''')

    def second_normal(self):
        if lingua in KO_KR:
            print(f'''
일반 채널을 선택하셨습니다.
''')
        elif lingua in EN_GB:
            print(f'''
You have selected a normal channel.
''')
    
    def second_live(self):
        if lingua in KO_KR:
            print(f'''
베스트 라이브 채널을 선택하셨습니다.
''')
        elif lingua in EN_GB:
            print(f'''
You have selected the Best Live channel.
''')

    def finish_phrase(self):
        df.info()
        if lingua in KO_KR:
            print(f'''
arcalive_{channel}_page_{n}_{creation_date}.csv가 저장되었습니다.
아카라이브 {channel} 채널의 최근 {n} 페이지 데이터 수집이 완료되었습니다.

제작자: EastPersiaLtd
''')
        elif lingua in EN_GB:
            print(f'''
Saving arcalive_{channel}_page_{n}_{creation_date}.csv has completed.
Data collecting of Arcalive {channel} channels latest {n} page(s) has(have) finished.

Credit: EastPersiaLtd
''')

    def limitation(self):
        if lingua in KO_KR:
            print(f'''
최대 10000 페이지 까지만 검색이 가능합니다. {pre_page} -> 10000
''')
        elif lingua in EN_GB:
            print(f'''
You can not search for greater than 1000 pages. {pre_page} -> 10000
''')

class desc3:
    def first(self):
        if lingua in KO_KR:
            print(f'''
NLP-K WordCloud 한국어 스크립트 {version}입니다.
NLP-K WordCloud용 스프레드시트 셀렉터를 실행합니다.
''')
        elif lingua in EN_GB:
            print(f'''
NLP-K WordCloud script {version} for English.
Execute spreadsheet selector for NLP-K WordCloud...
''')

    def second(self):
        if lingua in KO_KR:
            print(f'''
이 파일은 {type1} 형식입니다.
''')
        elif lingua in EN_GB:
            print(f'''
This file is {type1} format.
''')

    def third(self):
        if lingua in KO_KR:
            print(df.columns,'''
파일의 칼럼 리스트입니다.
''')
        elif lingua in EN_GB:
            print(df.columns,'''
Here is a coloumn list of the file.
''')

    def fourth(self):
        if lingua in KO_KR:
            print(f'''
준비가 완료되었습니다.
''')
        elif lingua in EN_GB:
            print(f'''
Preperation has completed.
''')


    def fifth(self):
        if lingua in KO_KR:
            print(f'''
NLP-K WordCloud 마법사 {version}입니다.

사용할 수 있는 컬러맵 종류는 아래와 같습니다.

계절
spring/summer/autumn/winter

그레디언트
viridis/plasma/inferno/magma/cividis
Wistia/cool/hot/afmhot/coolwarm
bwr/seismic/Spectral/twilight/twilight_shifted
ocean/gist_earth/gist_stern/terrain
CMRmap/cubehelix/gnuplot/gnuplot2

스펙트럼
hsv/brg/gist_rainbow/rainbow/jet
turbo/nipy_spectral/gist_ncar
''')
        elif lingua in EN_GB:
            print(f'''
NLP-K WordCloud Wizard {version}.

Here is the list of colourmaps as it follows.

-Season
spring/summer/autumn/winter

-Gradient
viridis/plasma/inferno/magma/cividis
Wistia/cool/hot/afmhot/coolwarm
bwr/seismic/Spectral/twilight/twilight_shifted
ocean/gist_earth/gist_stern/terrain
CMRmap/cubehelix/gnuplot/gnuplot2

-Spectrum
hsv/brg/gist_rainbow/rainbow/jet
turbo/nipy_spectral/gist_ncar
''')

    def sixth_custom(self):
        if lingua in KO_KR:
            print(f'''
지정된 경로의 폰트를 사용합니다.
''')
        elif lingua in EN_GB:
            print(f'''
Use custom font on the path.
''')

    def sixth_noncustom(self):
        if lingua in KO_KR:
            print(f'''
커스텀 폰트를 사용하지 않습니다. 경고: 차트가 깨질 수 있습니다.
''')
        elif lingua in EN_GB:
            print(f'''
Not using custom font. WARNING: CHART WILL NOT DISPLAY CLEARLY.
''')

    def finished(self):
        if lingua in KO_KR:
            print(f'''
nlp_k_wordcloud_arcalive_{channel}_page_{n}_{creation_date}.png가 저장되었습니다.
NLP-K WordCloud 생성이 끝났습니다.

제작자: EastPersiaLtd

''')
        elif lingua in EN_GB:
            print(f'''
Saving nlp_k_wordcloud_arcalive_{channel}_page_{n}_{creation_date}.png has completed.
Generating a NLP-K WordCloud chart has finished.

Credit: EastPersiaLtd

''')

    def terminate(self):
        if lingua in KO_KR:
            print(f'''
스크립트를 종료합니다.
''')
        elif lingua in EN_GB:
            print(f'''
Script has terminated.
''')
#####

#####Limitation on search page range
def limits(i):
    if i>10000:
        i:int=i-(i-10000)
        return i
    elif i<=10000:
        i:int=i
        return i

#####
desc=description()
desc3=desc3()

#####Select Channel
lingua=str(input(f'''
사용할 언어를 고르세요/Select the language you want. KO-KR / EN-GB: 
'''))
#####

if lingua in KO_KR:
    desc.first()
    channel=str(input(f'''
채널의 주소를 영문으로 입력하세요; https://arca.live/b/(채널 주소): 
'''))
#####
    n=int(input(f'''
스크래핑할 페이지의 범위를 입력하세요; 최근 n 페이지만큼-> n: 
'''))
#####
    pre_n=n
    n=limits(n)
    desc.limitation()
#####
    auto=int(input(f'''
Wordcloud 자동 생성을 활성화하시겠습니까?(KO-KR 폰트 필요) 0=아니오 / 1=네: 
'''))

elif lingua in EN_GB:
    desc.first()
    channel=str(input(f'''
Please input the channel address; https://arca.live/b/(channel address): 
'''))
#####
    n=int(input(f'''
Choose the range of pages you want to scrap; Collect the latest n pages -> n: 
'''))
#####
    pre_n=n
    n=limits(n)
    desc.limitation()
#####
    auto=int(input(f'''
Activate automatic Wordcloud generation?(KO-KR font required) 0=No / 1=Yes: 
'''))

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
df.to_csv(
    f'arcalive_{channel}_page_{n}_{creation_date}.csv',
    index=False,
    encoding="utf-8-sig"
)

#####Finished
desc.finish_phrase()

##########NLP-K
if auto==1:
    !pip install konlpy matplotlib wordcloud

    #####Import Packages
    from collections import Counter
    from konlpy.tag import Okt
    import matplotlib.pyplot as plt
    import os
    from wordcloud import WordCloud, STOPWORDS

    #####Wordcloud
    desc3.first()
    #####

    desc3.third()
    #####

    if lingua in KO_KR:
        column1=str(input('''
Wordcloud로 만들 칼럼을 지정해주세요(따옴표 생략): 
'''))
    elif lingua in EN_GB:
        column1=str(input('''
Select the column for generating a Wordcloud chart(You may ignore the inverted commas): 
'''))
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

#####
    if lingua in KO_KR:
        cmap=str(input('''
차트에 사용될 컬러맵을 골라주세요: 
'''))
        font_custom=str(input('''
차트에 사용하고 싶은 폰트의 위치를 입력하세요: 
'''))
    elif lingua in EN_GB:
        cmap=str(input('''
Select a colourmap for the chart: 
'''))
        font_custom=str(input('''
Select the path of custom font for the chart: 
'''))
#####

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

else:
    desc3.terminate()

#####
#sync=int(input('구글 드라이브와 연동하시겠습니까? 0: 아니오 / 1: 예'))
#if sync==1:
#    print('구글 드라이브와 연동합니다.')
#    from google.colab import drive
#    drive.mount('/content/drive')
#    print('구글 드라이브와 연동했습니다.')
#elif sync==0:
#    print('구글 드라이브와 연동하지 않습니다.')
#else:
#    print('잘못된 수치입니다. 다시 시도해주세요.')
#    sys.exit()
#####