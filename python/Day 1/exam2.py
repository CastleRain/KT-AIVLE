# chap2

# # 1) Bool 연산자
# if "a" == "A" or 10 == 10.0:
#     print("yes")
# else:
#     print("no")

# # 2)
# if 20 == 20.0 and "123" == "일이삼":
#     print("yes")
# else:
#     print("no")

# # 3)
# a = 30
# b = 40

# if a > b and a // b < 2:
#     print("yes")
# else: 
#     print("no")

# # 4
# c = 20
# d = 30
# if c + d > (c ** 2) or( c * d % 2) == 0:
#     print("yes")
# else:
#     print("no")

# #5
# v1 = 10
# v2 = 20
# v3 = 30

# if (v1 // v2) % 2 == 0 and( v2 + v3) % 2 != 0:
#     print("yes")
# else:  
#     print("no")

# 2) if

# 1
score = 92
if score > 90:
    print("pass")
else:
    print("non pass")

# 2
age = 27

if age < 10:
    print("10세 미만")
elif age < 20:
    print("20세 미만")
elif age < 30:
    print("30세 미만")
elif age < 40:
    print("40세 미만")
else:
    print("50세 미만")

# 3
score = 89

if score >= 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
elif score > 60:
    print("D")
else:
    print("F")

# 4
score1 = 42
score2 = 68
score3 = 98

if score1 < 70 or score2 < 70 or score3 < 70 or (score1 + score2 + score3)//3 < 75:
    print("fail")
else:
    print("pass")

# 5
num1 = 30
if num1%11 == 0:
    print("11의 배수입니다.")
else:
    print("11의 배수가 아닙니다.")

# 6
num1 = 20
num2 = 30
if num1>num2:
    print(num1)
    print(num2)
else:
    print(num2)
    print(num1)

# 7

num = int(input())
if num == 1:
    print("잘 했어요")
elif num == 2:
    print("정답")
elif num == 3:
    print("맞췄어요")
else:
    print("틀렸어요")


# 8
purchase = int(input())

if purchase >= 300000:
    print("VIP 등급 고객입니다. 10% 할인 쿠폰 지급해드립니다.")
elif purchase >= 150000:
    print("S 등급 고객입니다. 5% 할인 쿠폰 지급해드립니다.")
elif purchase >= 50000:
    print("A 등급 고객입니다. 2% 할인 쿠폰 지급해드립니다.")
else:
    print("Family 등급 고객입니다.")