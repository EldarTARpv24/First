from math import *
from random import *
#upper() - делает всё верхним регистром

#lower() - делает все нижним регистром
#capitalize() - делает первую букву в верхний регистр
# date.today()
# strftime()
# tana = tana.strftime("%d/%m/%Y")

# print(3 + 8 / (4 - 2) * 4)
#19

# print(3 + 8 / 4 - 2 * 4)
#-3

# from math import *
# try:
#     r = float(input("Введите радиус: "))
#     scube = round((r * 2) ** 2, 2)
#     so = round(pi * r ** 2, 2)
#     pcube = round(r * 2 * 4, 2)
#     po = round(2 * pi * r,2)
# except:
#     print("Только цифры")
# print(f"Площади равны {scube} и {so}, Периметры равны {pcube} и {po}")

#Ul 4

# from math import *
# earth = 6378 #км
# coin = 2.575 #см
# earth *= 100000
# print(earth)
# c = pi * 2 * 6378
# kogus = c / coin
# print(f"Ответ равен:, {int(kogus):,d}Ответ равен:, {int(kogus):,d}")

#Ul 5

# a = "kill-koll ".capitalize()
# b = "killad-koll ".capitalize()
# print(a*2 , b , a * 2 , b , a*4)

#UL 7
# try:
#     a = float(input("Одна сторона: "))
#     b = float(input("Вторая:"))
#     if a > 0 and b> 0:
#         p = (a + b) / 2
#         s = a*b
#         print(f"S={s}, P={p}")
#     else:
#         print("неверное значение")
# except:
#     print("Ошибочные значения")

#Ul 8
# try:
#     lit = float(input("Количество литров:"))
#     road = float(input("Путь равен:"))
#     if lit > 0 and road > 0:
#     ans = (lit / road) * 100
#     print(ans)
# except:
#     print("Неверное значение")

#UL 9 

# try:
#     m = int(random.randint(1, 100))
#     if m >= 0:
#         kmh = float(29.9)
#         kmm = kmh * 1000/ m
#         print(kmm)
# except:
#     print("Ошибка")

# UL 9
# m = int(randint(1, 100))
# try:
#     if m >= 0:
#         print(m)
#         kmh = float(29.9)
#         kmm = kmh * 1000/ m
#         print(kmm)
#     else:
#         print("ошибка")
# except:
#     print()

#Ul 10

try:
    time = int(input("Введите время в минутах"))
    if time >= 60:
        a = time // 60
        b = time % 60
        print(f"Сейчас {a}: {b}")

 
except:
    print("Ошибка")