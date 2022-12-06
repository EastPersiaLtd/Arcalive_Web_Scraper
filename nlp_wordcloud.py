#@title TEST C
#####1.0.3

!pip install collections konlpy matplotlib pandas pyreadstat wordcloud

##########Import Packages
from collections import Counter
from konlpy.tag import Okt
import matplotlib.pyplot as plt
import os
import pandas as pd
import sys
import time
from wordcloud import WordCloud, STOPWORDS

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

#####
desc3=desc3()

#####
creation_date=str(time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time())))

desc3.first()
#####
file1=str(input('파일 위치를 입력해주세요: '))
type1=str(os.path.splitext(file1)[1])
desc3.second()
#####
if type1=='.csv':
    df=pd.read_csv(file1)
elif type1=='.xlsx' or '.xls':
    df=pd.read_excel(file1)
elif type1=='.spss':
    df=pd.read_spss(file1)
else:
    print('이 파일은 지원되지 않는 형식입니다. 다시 시도해주세요.')
    sys.exit()
#####
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