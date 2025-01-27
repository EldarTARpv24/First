#upper() - делает всё верхним регистром
#lower() - делает все нижним регистром
#capitalize() - делает первую букву в верхний регистр

# print(3 + 8 / (4 - 2) * 4)
#19

# print(3 + 8 / 4 - 2 * 4)
#-3

from math import *
try:
    r = float(input("Введите радиус: "))
    scube = round((r * 2) ** 2, 2)
    so = round(pi * r ** 2, 2)
    pcube = round(r * 2 * 4, 2)
    po = round(2 * pi * r,2)
except:
    print("Только цифры")
print(f"Площади равны {scube} и {so}, Периметры равны {pcube} и {po}")
