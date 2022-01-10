# # chap 3

# # 1
# print(list(range(21)))

# # 2
# print(list(range(1, 21)))

# # 3
# print(list(range(5, 101, 5)))

# # 4
# print(list(range(3, 61, 4)))

# # 5
# print(list(range(200, 9, -10)))

# # 6
# print(list(range(160, 9, -30)))

# # 7
# print(list(range(-2, -11, -1)))

# # 8
# print(list(range(5, -16, -3)))

# # 2)

# # 1
# for i in range(6):
#     print(i)

# # 2
# for i in range(1,6):
#     print("*" * i)

# # 3
# for i in range(1, 6):
#     print(" " * (5-i) + "*"*i)

# # 4
# for i in range(1, 6):
#     if i % 2 == 0:
#         print("%" * i)
#     else:
#         print("*" * i)

# # 5
# reuslt = 0
# for i in range(100):
#     reuslt += (i + 1)
# print(reuslt)

# # 6
# reuslt = 0
# for i in range(1, 101):
#     if i % 2 != 0:
#         reuslt += i
# print(reuslt)

# # 7
# result = 0
# for i in range(1, 501):
#     if i % 12 == 0:
#         result += i

# print(result)

# # 8
# result = 0

# for i in range(1, 101):
#     if i % 2 != 0:
#         result += i
#     else:
#         result -= i
# print(result)

# # 9
# num = int(input("숫자를 입력하세요 : "))
# name = input("이름을 입력하세요 : ")

# print(name * num)

# # 10
# name = input('이름을 입력하세요 : ')
# for n in name:
#     print(n)

# # 11
# num = int(input("숫자를 입력하세요 : "))
# name = input("이름을 입력하세요 : ")

# if num >= 10:
#     print("너무 많아요" * 4)
# else:
#     print(name * num)

# # 12
# for i in range(2, 10):
#     print(f"구구단 {i}단을 출력합니다.")

#     for j in range(1, 10):
#         print(f"{i} * {j}  = {i*j}")
#     print("\===========")

# # 13
# input_n = int(input("구구단 시작지점을 적어주세요 : "))
# for i in range(input_n, 10):
#     print(f"구구단 {i}단을 출력합니다.")

#     for j in range(1, 10):
#         print(f"{i} * {j}  = {i*j}")
#     print("\===========")

# # 14
# up_down = input("올라갈까요 내려갈까요 : ")
# if up_down == "up":
#     num = int(input("숫자 입력 : "))
#     for i in range(1, num+1):
#         print(i)
# elif up_down == "down":
#     num = int(input("20이하 숫자 : "))
#     for j in range(20, num-1, -1):
#         print(j)
# else:
#     print("틀렸어요")

# # while loop
# # 1
# i = 0
# while i<6:
#     print(i)
#     i+= 1

# # 2
# i = 1
# while i<6:
#     if i % 2 == 0:
#         print("%" * i)
#     else:
#         print("*" * i)
#     i+=1
    
# # 3
# i = 1
# result = 0
# while i < 101:
#     if i % 3 == 0:
#         result += i
#     i += 1
# print(result)

# # 4

# num = int(input("num : "))
# sentence = input("sentence : ")

# while num > 0:
#     print(sentence)
#     num -= 1

# # 5
# name = input("이름 : ")

# if name == "장성우":
#     print("hello")
# else:
#     print("who are you")

# # 6
# total = 0

# while True:
#     if total <= 50:
#         num = int(input("num : "))
#         total += num
#         print(f"totla value는 {total}이다.")
#     else:
#         break

# # 7
# kor, math, eng = 96, 72, 88
# n = input("보고싶은 것 입력 : ")
# if n == "국어":
#     print(kor)
# elif n == "수학":
#     print(math)
# elif n == "영어":
#     print(eng)
# else:
#     print("잘못입력되었습니다.")

# # 8
# input_n = int(input("input_n : "))
# think_n = int(input("think_n : "))

# if input_n != think_n:
#     if input_n < think_n:
#         print("input_n이 더 작습니다")
#     else:
#         print("think_n이 더 작습니다.")
# else:
#     print("참 잘했어요")

# 9

money = int(input("돈을 입력해주세요:"))
coffee = 1300
while True:
    if input("아메리카노를 구입하시겠습니까? ") == "네":
        if money < 1300:
            print("돈이 모자랍니다. 커피를 구입할 수 없습니다.")
            break
        else:
            money -= 1300
            print(f"감사합니다. 현재 남은돈은 {money}입니다.")

    else:
        print("다시 입력해주세요. ")