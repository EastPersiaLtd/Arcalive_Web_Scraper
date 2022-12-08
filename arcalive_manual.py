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
#####
#####
desc=description()

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