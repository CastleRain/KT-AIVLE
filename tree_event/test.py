# from konlpy.tag import Okt
# okt = Okt()

# print(okt.pos('아버지가 방에 들어가신다'))
# print(okt.pos('아버지가방에들어가신다'))

from konlpy.tag import Okt
from collections import Counter
okt = Okt()

aivle = ['에이', '블', '스쿨']

file = open("KT_AIVLE.txt", "r", encoding="UTF-8") 
file_txt = file.read()
file_txt_noun = okt.nouns(file_txt)

file.close()


for i,v in enumerate(file_txt_noun):
    if len(v) < 2:
        file_txt_noun.pop(i)

    count = Counter(file_txt_noun)

print(count)



# counter = Counter(t)
# # print(t)
# counter.update({'KT AIVLE' : 233})
# print(counter)

# 에이 블 스쿨 -> KT AIVLE