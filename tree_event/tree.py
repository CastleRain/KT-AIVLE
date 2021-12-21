from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
# 한글 폰트 패스로 지정
import matplotlib.font_manager as fm
import re
import collections
import numpy as np
from PIL import Image

from konlpy.tag import Okt
from collections import Counter

okt = Okt()

# aivle = ['에이', '블', '스쿨']

file = open("KT_AIVLE.txt", "r", encoding="UTF-8") 
file_txt = file.read()
file_txt_noun = okt.nouns(file_txt)

file.close()


for i,v in enumerate(file_txt_noun):
    if len(v) < 2:
        file_txt_noun.pop(i)

    count = Counter(file_txt_noun)

count.update({'KT AIVLE' : 100, "Merry Christmas" : 100})


tree_mask = np.array(Image.open('tree_event/img/Tree_white4.png'))
image_colors = ImageColorGenerator(tree_mask)


wc1 = WordCloud(max_font_size=100, mask = tree_mask,mode = "RGBA", 
                background_color="#143338", width=1000, height=1000, font_path="tree_event/font/BMDOHYEON.ttf"
                , repeat=True)
wc1.generate_from_frequencies(count)

wc1.recolor(color_func = image_colors)

plt.figure(figsize=(10, 8))

plt.imshow(wc1)

plt.tight_layout(pad=0)
plt.axis('off')
plt.show()
