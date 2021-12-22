# 필요 모듈
from os import remove
import re
from collections import Counter
import numpy as np

# word cloud를 위한 모듈
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from PIL import Image

# 한글 전처리 모듈
from konlpy.tag import Okt


# 1. kt aivle로 검색하여 나온 블로그 글 가져오기 (네이버, 다음, 구글)

"""
참고 페이지 : 
1) https://blog.naver.com/porory_rei/222597404726
2) https://blog.naver.com/aa5002021/222598422272
3) https://castlerain.tistory.com/25

"""
file = open("KT_AIVLE.txt", "r", encoding="UTF-8") 
file_txt = file.read()
file.close()

# 2. 한글 전처리를 위해 konlpy의 okt 사용

okt = Okt()
file_txt_noun = okt.nouns(file_txt)

## 2.1 2글자 이상인 데이터만 추출

for i,v in enumerate(file_txt_noun):
    if len(v) < 2:
        file_txt_noun.pop(i)

    ko_noun_txt = Counter(file_txt_noun)




## 2.2 삭제, 추가하고 싶은 데이터 전처리

"""
'에이블 스쿨' 이라고 입력 된 데이터가 명사로 끊기면서 '에이' '블' '스쿨'로 나오는 것을 확인하고 삭제를 진행했다. 
해당 데이터마다 KT AIVLE을 추가 하고 싶었지만 결과 그림에 더 크게 나오게 하고 싶어서 update를 통해 추가 진행을 해주었다.

"""
remove_word = ['에이', '블', '스쿨']

for re_w in remove_word:
    del(ko_noun_txt[re_w])

ko_noun_txt.update({'KT AIVLE' : 200, "Merry Christmas" : 190})


# 3. word cloud 진행

## 3.1 나무 모양을 위한 이미지 가져오기

tree_mask = np.array(Image.open('tree_event/img/Tree_white5.png'))
image_colors = ImageColorGenerator(tree_mask)


### font_size는 100이상은 다 비슷한것 같다.

tree_wc = WordCloud(max_font_size=200, 
                    mask = tree_mask,mode = "RGBA", 
                    background_color="#143338",
                    width=1000, 
                    height=1000, 
                    font_path="tree_event/font/BMDOHYEON.ttf",
                    repeat=True).generate_from_frequencies(ko_noun_txt)

tree_wc.recolor(color_func = image_colors)

plt.figure(figsize=(10, 8))
plt.imshow(tree_wc)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()
