!pip install bs4 pandas

##########Import Packages
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

#####Create the lists
post_title=[]
post_author=[]
post_time=[]
post_url=[]

#####Select Channel
print('아카라이브 웹 스크래퍼입니다.\n주요 채널 목록은 아래와 같습니다.\n')
#####
print('원신/genshin:  6400p/month\n블루아카이브/bluearchive:  4500p/month\n붕괴3rd/hk3rd:  2400p/month\n카운터사이드/counterside:  2000p/month')
print('던전앤파이터/dunfa:  1800p/month\n명일방주/arknights:  1600p/month\n라스트오리진/lastorigin:  900p/month\n벽람항로/azurlane:  750p/month')
print('프린세스 커넥트 Re:Dive/prcn:  300p/month\n')
#####
channel=str(input('채널의 주소를 영문으로 입력하세요; https://arca.live/b/(채널 주소): '))
#####
n=int(input('크롤링할 페이지의 범위를 입력하세요; 최근 n 페이지만큼-> n:'))
#####
creation_date=str(time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time())))

#####Clause 1-1: General Channel
if channel!='live':
    print('일반 채널을 선택하셨습니다.')
    for i in range(n):
        url=f'https://arca.live/b/{channel}?p={i+1}'
        #####
        response=requests.get(url)
        soup=BeautifulSoup(response.text, 'html.parser')
        #####
        if n==1:
            n1=list(range(14, 59, 1))
            for i in range(len(n1)):
                title=soup.select('span.title')
                #####
                author_selector=str(f'div.list-table.table > a:nth-of-type({n1[i]}) > div.vrow-inner > div.vrow-bottom > span.vcol.col-author > span.user-info')
                author=soup.select(author_selector)
                #####
                time_selector=str(f'div.list-table.table > a:nth-of-type({n1[i]}) > div > div.vrow-bottom > span.vcol.col-time')
                time=soup.select(time_selector)
                #####
                url_selector=str(f'div.list-table.table > a:nth-of-type({n1[i]}) > vrow.column')
                url=soup.select(url_selector)
                #####
                for j in title:
                    post_title.append(j.get_text())
                for k in author:
                    post_author.append(k.get_text())
                for l in time:
                    post_time.append(l.attrs['datetime'])
                for m in url:
                    post_url.append(m.attrs['href'])
        #####
        else:
            n2=list(range(4, 49, 1))
            for i in range(len(n2)):
                #####
                title=soup.select('span.title')
                #####
                author_selector=str(f'div.list-table.table > a:nth-of-type({n2[i]}) > div.vrow-inner > div.vrow-bottom > span.vcol.col-author > span.user-info')
                author=soup.select(author_selector)
                #####
                time_selector=str(f'div.list-table.table > a:nth-of-type({n2[i]}) > div > div.vrow-bottom > span.vcol.col-time > time')
                time=soup.select(time_selector)
                #####
                url_selector=str(f'div.list-table.table > a:nth-of-type({n2[i]}) > vrow.column')
                url=soup.select(url_selector)
                #####
                for j in title:
                    post_title.append(j.get_text())
                for k in author:
                    post_author.append(k.get_text())
                for l in time:
                    post_time.append(l.attrs['datetime'])
                for m in url:
                    post_url.append(m.attrs['href'])

#####Clause 1-2: Best Live Channel
elif channel=='live':
    print('베스트 라이브 채널을 선택하셨습니다.\n베스트 라이브 채널은 현재 작성자 수집에 에러가 있습니다.')
    for i in range(n):
        url=f'https://arca.live/b/{channel}?p={i+1}'
        #####
        response=requests.get(url)
        soup=BeautifulSoup(response.text, 'html.parser')
        #####
        n2=list(range(4, 49, 1))
        for i in range(len(n2)):
            #####
            title=soup.select('a.title')
            #####
            author_selector=str(f'div.list-table.hybrid > div:nth-child({n2[i]}) > div.vrow-inner > div.vrow-bottom > span.vcol.col-author > span.user-info')
            author=soup.select(author_selector)
            #####
            time_selector=str(f'div.list-table.hybrid > div:nth-of_type({n2[i]}) > div.vrow-inner > div.vrow-bottom > span.vcol.col-time > time')
            time=soup.select(time_selector)
            #####
            url_selector=str(f'div.list-table.hybrid > div:nth-of_type({n2[i]}) > div.vrow-inner > div.vrow-top > span.vcol.col-title > a')
            url=soup.select(url_selector)
            #####
            for j in title:
                post_title.append(j.get_text())
            for k in author:
                post_author.append(k.get_text())
            for l in time:
                post_time.append(l.attrs['datetime'])
            for m in url:
                post_url.append(m.attrs['href'])

#####List JOIN
post_list = list(zip(post_title, post_author, post_time, post_url))
col=['post_title', 'post_author', 'post_time', 'post_url']

#####DataFrame conversion
df=pd.DataFrame(post_list, columns=col)
df=df.replace(r'\n', '', regex=True)
df.to_csv(f'arcalive_{channel}_page_{n}_{creation_date}.csv', index=False, encoding="utf-8-sig")

#####Finished
print(f'arcalive_{channel}_page_{n}_{creation_date}.csv의 저장이 완료되었습니다.')
print(f'아카라이브 {channel} 채널의 최근 {n} 페이지 데이터 수집이 완료되었습니다.\n제작자: EastPersiaLtd\n')