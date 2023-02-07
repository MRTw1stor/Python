from math import sin, cos, pi
import numpy as np
a = float(input("Введите начало диапазона - a (a*pi): "))*pi
b = float(input("Введите начало диапазона - b (b*pi): "))*pi
h = pi/float(input("Введите значение шага - h (pi/h): "))
print(" ")
print("Таблица згачений функции y:")
print("№      x       y       Направление        Разность")
s = 0
d = 0
min = 0
max = 0
for x in np.arange(a,b,h):
    y = exp(x)*sin(x)
    s = s+1
    if (y>d):
        Changes = "Возрастает"
    elif (y==d):
        Changes = "Неменяеться"
    else:
        Changes = "Убывает"
    Difference = y-d
    d=y
    if(y>max):
        max = y
    if (y<min):
        min = y
    print("%3s"%s," ","%7s"%("%.3f"%x)," ","%7s"%("%.3f"%y)," ","%10s"%Changes," ","%7s"%("%.3f"%Difference))
print("min y =",".3f"%min," ","max y=",".3f"%max)