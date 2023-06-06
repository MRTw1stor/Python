from random import randint
a = int(input("Введите количество столбцов:"))
b = int(input("Введите начало диапазона:"))
c = int(input("Введите конец диапазона:"))
massiv = [randint(b,c) for i in range(a)]
print("Дан массив: ", massiv)
sum = 0
for element in massiv:
    if element <= 20:
        sum = sum + element
print("Сумма элементов массива значение которых не превышает 20: " , sum)
x = float(input("Введите первое число для сравнения: "))
suma = 0
for element in massiv:
    if element > x:
        suma = suma + element
print("Сумма элементов массива которые больше","%.d" % x,":", suma)
y = float(input("Введите второе число для сравнения: "))
summa = 0
for element in massiv:
    if element % x == 0 or element % y == 0:
        summa = summa + element
print("Сумма элементов массива которые кратны","%.d" % x,"или","%.d" % y,":", summa)