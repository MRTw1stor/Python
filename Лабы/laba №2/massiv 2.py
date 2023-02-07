from random import randint
a = int(input("Введите количество строк"))
b = int(input("Введите количество столбцов:"))
c = int(input("Введите начало диапазона:"))
d = int(input("Введите конец диапазона:"))
massiv = [[randint(c,d) for i in range(b)]for j in range(a)]
print("Дан массив:",massiv)
sum = 0
col = 0
for i in range(len(massiv)):
    if massiv[i][2] % 2 == 0:
        col = col + 1
        sum = sum + (massiv[i][2])
print("Среднее арифметическое четных элементов третьего столбца:","%.3f" %(sum/col))
summ = 0
kol = 0
for j in range(len(massiv[3])):
    if massiv[3][j] %3 == 0:
        kol = kol + 1
        summ = summ + massiv[3][j]
print("Среднее арифметическое элементов четвертой строки, кратных трем:","%.d" %(summ / kol))