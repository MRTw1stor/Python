from math import cos
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
y = float(input("Введите число y: "))
s = ((a*y+57)**(1/3))/(3+abs(cos(b))+(a*y+57)**(1/3))
print("Ответ =","%.3f" %s)