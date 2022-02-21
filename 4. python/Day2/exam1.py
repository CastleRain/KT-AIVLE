# # chap4

# # 1
# a = [1,2,3,4,5]
# print(a)

# # 2
# b = ['ab', 'cd' , 'ef']
# print(b)

# # 3
# c = [123, 'ab', 45, 'cde']
# print(c)

# # 4
# list_a = [1,3,5,7,9]
# list_b = [1, 'a', 3, 'b']
# print(list_a)
# print(list_b)

# # 5
# d = [i for i in range(21)]
# print(d)

# # 6
# list_c = [i for i in range(1, 20) if i % 3 == 1]
# print(list_c)

# # 7
# list_d = [1,2,3]
# list_e = list_d + [4,5]
# print(list_e)

# # 8
# list1 = [1, 3, 'hello']
# list2 = list1 + ['happy', 2,4]
# print(list2)

# # 2 리스트 사용하기

# # 1
# list1 = [1,2,3,4,5]
# print(list1[0], list1[-1])

# # 2
# a = [23, 3, 16, 45, 11]
# print(a[0], a[3])
# print(a[-1], a[-3])

# # 3
# list1 = [1,3,5,7]
# list2 = [2,4,8] + [list1[1]]

# # 4
# list1 = [1,3,5,7]
# list2 = [2,4,8]
# list2 += list1
# print(list2)

# # 5
# a = [23, 3, 16,45, 11]
# print(a[:3])
# print(a[2:4])
# print(a[2:])

# print(a[-3:-1])
# print(a[-4:-1])
# print(a[-3:])
# print(a[-5])

# #3 리스트 수정하기

# # 1
# a = [23, 3, 16, 45, 11]
# a.append(99)

# # 2
# a = [23, 3, 16, 45, 11]
# a.append(99)
# b = [100]
# b += a
# print(b)

# # 3
# list1 = [1,3,5,7]
# list2 = [2,4,8]
# list2.append(list1[1])

# # 4
# list1 = [1,3,5,7]
# list2 = [2,4,8]
# list2 = list1 + list2

# # 5
# a = [23, 3, 16,45, 11]
# print(a[1])
# a[1] = 300
# print(a[1])

# # 6
# a = [23, 3, 16, 45, 11]
# print(a[-1])
# a[-1] *= 2
# print(a[-1])

# # 7
# a = [23, 3, 16, 45, 11]
# del a[1]

# # 4 리스트에 사용하는 함수

# # 1
# list2 = [n for n in range(1, 20) if n % 3 == 1]
# print(len(list2))

# # 2
# list3 = ['python' ,'is' ,'funny']
# print(len(list3))

# # 3
# list2 = [n for n in range(1, 100) if n % 7 == 0]
# print(sum(list2))

# # 4
# list1 = [10, 20, 30, 40, 50]
# print(type(list1))

# # 5
# num = [10, 21, 34, 47, 53]
# print(sum(num) / len(num))

# # 5 리스트에 사용하는 메서드

# # 1 
# list1 = [10, 20, 30, 40, 50]
# list1.append(60)

# # 2
# list3 = ['python', 'is', 'funny']
# list3.append("~")
# list3.append("!")

# # 3
# list1 = [10, 20, 30, 40, 50]
# list1.insert(2, 60)
# print(list1)

# # 4
# list3 = ['python' ,'is', 'funny']
# list3.insert(3, 'very')

# # 5
# list1 = [10, 20, 30, 40, 50]
# list1.remove(30)
# print(list1)

# # 6
# list2 = [n for n in range(1, 21, 3)]
# del list2[-3]
# print(list2)

# # 7
# a = [1, 4, 3, 2]
# a.sort()
# print(a)

# # 8
# b = ['c', 'a' ,'b' ,'d']
# b.sort(reverse=True)
# print(b)

# # 9
# sports = ['주짓수' ,'무에타이']
# name = input("좋아하는 스포츠를 입력하세요 : ")
# sports.append(name)
# sports.sort()
# print(sports)

# # 10
# subjects = ['국어' ,'영어', '수학', '한국사', '물리' ,'화학']
# name = input("실헝하는 과목을 입력하세요 : ")
# subjects.remove(name)
# print(subjects)

# # 6 리스트와 for loop

# animal = ['사자' ,'코끼리', '하마', '기린', '얼룩말']

# for i in animal:
#     print(i)

# # 2
# dizney = ['인어공주', '알라딘', '겨울왕국' ,'라푼젤']
# dizney.append('라이언킹')
# for i in dizney:
#     print(i)

# # 3
# multiple7 = []

# for i in range(1, 100):
#     if i % 7 == 0:
#         multiple7.append(i)
# print(multiple7)

# # 4
# my_list = []
# for _ in range(5):
#     my_list.append(int(input('입력 : ')))
# my_list.sort()
# print(my_list)

# # 5
odd, even = [], []
for _ in range(10):
    data = int(input('입력 : '))
    if data % 2 == 0:
        even.append(data)
    else:
        odd.append(data)

print(even)

print(odd)
