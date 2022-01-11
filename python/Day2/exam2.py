# chap 5

# 1
dict_a = {
    'v1' : 32,
    '11' : [1,2,3],
    'd1' : {
        'a' : 1,
        'b' : 2
    } 
}
# print(dict_a)

# 2
dict_2 = {
    '이름' : '이희성',
    '나이' : 38,
    '전공' : '기계공학',
    '사용 언어' : ['기계어', '어셈블리어', 'C++']
}

# # 3
# print(dict_a['v1'])
# print("###################")
# print(dict_a['11'][:])
# print(dict_a['11'][:2])
# print("###################")
# print(dict_a['d1'])
# print(dict_a['d1']['a'])

# # 4
# print(dict_a.get('v1'))

# for key, value in dict_a.items():
#     print('key : ', key)
#     print('value : ', value)

# # 5
# animals = ['사자', '코끼리', '하마']

# a1, a2, a3 = animals
# print(a1, a2, a3)

# # 6
# movies = ['인어공주' ,'알라딘' ,'겨울왕국', '라푼젤']
# m1, m2, m3, m4 = movies
# print(m1, m2, m3, m4)

# # 7
# i1, i2, i3 = dict_a.values()
# print(i2, i3)
# print(i2[-1])
# print(i3['b'])

# # 8
# dict_a['v2'] = 500

# del dict_a['v1']

# # 9
# if 'v1' in dict_a.keys():
#     print(dict_a['v1'])

# if 'v2' in dict_a.keys():
#     print(dict_a['v2'])
# else:
#     print(dict_a.get('v2', 0))

# 10
# for key, value in dict_a.items():
#     print('key : ', key)
#     print('value : ', value)

# # 11

# icecream = {
#     '메로나' : [400, 380],
#     '비비빅' : [400, 350],
#     '탱크보이' : [500, 450],
#     '월드콘' : [1000, 900]

# }

# weekday = ['월', '화', '수', '목', '금']
# day = input("요일을 입력하세요 : ")

# if day in weekday:
    
#     for key, value in icecream.items():
#         print(key, "의 가격은 " , value[0])
# else:
#     for key, value in icecream.items():
 #       print(key, "의 가격은 " , value[1])

# 12
from collections import defaultdict

dic = defaultdict(int)

lyrics = input("팝송을 입력하세요 : ")
print(lyrics)
lyrics = lyrics.lower()

for i in lyrics:
    dic[i] +=1


print(dic)