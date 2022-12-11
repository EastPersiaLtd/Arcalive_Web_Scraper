#@title TEST C

!pip install konlpy matplotlib pandas pyreadstat wordcloud

##########Import Packages
from collections import Counter
from konlpy.tag import Okt
import matplotlib.pyplot as plt
import os
import pandas as pd
import sys
import time
from wordcloud import WordCloud, STOPWORDS

KO_KR=['KO_KR', 'ko_kr', 'KO-KR', 'KO-kr', 'Ko-Kr', 'Ko-kr', 'ko-Kr', 'ko-KR', 'ko-kr', 'KR', 'kr', 'Korea', 'Korean', 'korea', 'korean', 'Hangeul', 'hanguel',
'한국어', '한글', '한국말', 'gksrnrdj', 'gksrmf', 'gksrnrakf']
EN_GB=['EN_GB', 'en_gb', 'EN-GB', 'EN-gb', 'En-Gb', 'En-gb', 'en-Gb', 'en-GB', 'en-gb', 'EN-US', 'en-us', 'English', 'english', 'ENG', 'eng', 'not american']

version=(f'1.0.4')

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
#####

#####
desc3=desc3()

#####Choose a language
lingua=str(input(f'''
사용할 언어를 고르세요/Select the language you want. KO-KR / EN-GB: 
'''))

desc3.first()
#####
creation_date=str(time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time())))

#####Read the file
if lingua in KO_KR:
    file1=str(input('''
파일 위치를 입력해주세요: 
'''))
elif lingua in EN_GB:
    file1=str(input('''
Please input the path of the file: 
'''))
#####

#####Read the format of file
type1=str(os.path.splitext(file1)[1])
desc3.second()

#####File format check
if type1=='.csv':
    df=pd.read_csv(file1)
elif type1=='.xlsx' or '.xls':
    df=pd.read_excel(file1)
elif type1=='.spss':
    df=pd.read_spss(file1)
else:
    if lingua in KO_KR:
        print('''
이 파일은 지원되지 않는 형식입니다. 다시 시도해주세요.
''')
    elif lingua in EN_GB:
        print('''
This file format does not supported. Please try again.
''')

    sys.exit()
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
plt.savefig(f'nlp_k_wordcloud_{creation_date}.png')

#####Show the chart
plt.show()

#####Finished 2
desc3.finished()