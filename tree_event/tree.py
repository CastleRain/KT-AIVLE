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

remove_word = ['에이', '블', '스쿨']

for re_w in remove_word:
    del(ko_noun_txt[re_w])

ko_noun_txt.update({'KT AIVLE' : 100, "Merry Christmas" : 100})


# 3. word cloud 진행

## 3.1 나무 모양을 위한 이미지 가져오기

tree_mask = np.array(Image.open('tree_event/img/Tree_white5.png'))
image_colors = ImageColorGenerator(tree_mask)


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

# plt.tight_layout(pad=0)
plt.axis('off')
plt.show()
