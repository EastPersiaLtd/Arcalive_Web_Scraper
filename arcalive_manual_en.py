#@title TEST B
#####1.0.3

!pip install bs4 pandas

##########Import Packages
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

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

class inputs:
    def __init__(self):
        self.first_ko=0
        self.channelk0=0
        self.nk0=0
        #####
        self.first_en=print('Arcalive Web Scraper 1.0.3.\n\nHere is the list of major channels as it follows.\n\nGenshin Project/genshin:  6400p/month\nBlue Archive/bluearchive:  4500p/month\nHonkai 3rd/hk3rd:  2400p/month\nCounterside/counterside:  2000p/month\nDNF/dunfa:  1800p/month\nArknights/arknights:  1600p/month\nLast Origin/lastorigin:  900p/month\nAzur Lane/azurlane:  750p/month\nPrincess Connect Re:Dive/prcn:  300p/month\n')
        self.channele0=input('Please input the channel address; https://arca.live/b/(channel address): ')
        self.ne0=input('Choose the range of pages you want to scrap; Collect the latest n pages -> n: ')
#####
    
    def first(self):
        self.first_enx=self.first_en
        self.first_kox=self.first_ko

    def channelx1(self):
        self.channelx1=self.channele0

    def nx1(self):
        self.nx1=self.ne0

    #def printinp(self):
        #print(f'{inputs.channelx1} 채널입니다. {inputs.nx1} 페이지 만큼 찾습니다.')
#####

#####
desc1=desc1()
desc2=desc2()
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
    desc2.second_normal()
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
    desc2.second_best()
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
desc2.finished()