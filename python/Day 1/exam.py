"""
chap1
"""
# 1) print()사용하기

# # 1
# print(123456)

# # 2
# print(123, end = " ")
# print(456)

# # 3
# print(123, 456)

# # 4
# print("파이썬을 배웁시다.")

# # 5
# print("파이썬을 배웁시다.", end = " ")
# print("누구든 할 수 있습니다.")

# # 6
# print("파이썬을 배웁시다.", "누구든 할 수 있습니다.")

# # 7
# print(123, end = " ")
# print("올해는", end = " ")
# print("2022년입니다.")

# # 8
# print(123, "올해는","2022년입니다.")

# # 2) 숫자 다루기

# n1 = 125
# n2 = 5

# # 1
# print(n1 + n2)
# print(n1 - n2)
# print(n1 * n2)
# print(n1 / n2)

# # 2
# print(178 // 13)

# # 3
# print(3854 // 11)

# # 4
# print(178 % 13)

# # 5
# print(3854 % 11)

# # 6
# if 563421 % 3 == 0: print("3의배수입니다.")

# # 7
# print(2**10)

# # 8
# print(6**-3)

# # 9

# if 652 > 87: print("큽니다.")

# # 10

# if 31 == 31.0: print("같습니다.")
# else: print("같지 않습니다.")
# # 10

# if 24 != 24.0: print("같지 않습니다.")
# else: print("같습니다.")

# # 문자 다루기

# # 1
# print("나는" +  "너를...")

# # 2
# print("나는","너를...")

# # 3
# print("*" * 10)

# # 4
# print("안녕하세요?" * 3 , "반갑습니다!" * 2)

# # 5
# if "a" > "b":
#     print("a가 더 큽니다.")
# else:
#     print("b가 더 큽니다.")

# #6
# if "a" > "A":
#     print("a가 더 큽니다.")
# else:
#     print("A가 더 큽니다.")

# #7
# if "가" > "나":
#     print("가가 더 큽니다.")
# else:
#     print("나가 더 큽니다.")

# #8
# if "abc" == "ABC":
#     print("같습니다")
# else:
#     print("다릅니다.")

# #9
# if "가나다" != "ABC":
#     print("다릅니다")
# else:
#     print("같습니다..")

# 4) 변수

# 1
v1 = 48
v2 = "이희성"

print(v1)
print(v2)


# 2
a = 30
b = 40

print(a*b)

# 3
a = 30
b = 40
c = a + b
d = a * b

if c > d:
    print("덧셈이 더 큽니다.")
else:
    print("곱셈이 더 큽니다.")

# 4
e = 4
print("안녕하세요?" * e)

# 5
g1 = 1
g1 += 1

# 6
h = 2
h *= 2

# 7
i = 6
i **= 2

#8
kor = 96
math = 72
eng = 88

avg = (kor + math + eng) // 3
print(f"이희성 평균 점수는 {avg}")
