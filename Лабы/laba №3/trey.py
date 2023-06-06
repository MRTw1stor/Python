# функция для создания треугольника
trey = []
def treugolnik():
    global trey
    trey = []
    for i in range(3):
        stor = float(input("Введите "+str(i+1)+" сторону треугольника: "))
        trey.append(stor)
# проверяем существует-ли треугольник
    if trey[0] + trey[1] <= trey[2] or trey[2] + trey[1] <= trey[0] or trey[0] + trey[2] <= trey[1]:
        print("Такого треугольника не существует")
        treugolnik()
    if trey[0] == 0 or trey[1] == 0 or trey[2] == 0:
        print("Такого треугольника не существует")
        treugolnik()
# функция нахождения периметра треугольника
perim = 0
def P(a,b,c):
    global perim
    perim = a + b + c
# функция нахождения площади треугольника
square = 0
def S(a, b, c, perimetr):
    global square
    semiperim = perimetr/2
    square =(semiperim *(semiperim-a)*(semiperim-b)*(semiperim-c)) ** (0.5)
# вызов функций для нахождения значений
print("Введите стоноры первого треугольника")
treugolnik()
P(trey[0],trey[1],trey[2])
S(trey[0],trey[1],trey[2], perim)
perim1 = perim
square1 = square
print("Введите стоноры второго треугольника")
treugolnik()
P(trey[0],trey[1],trey[2])
S(trey[0],trey[1],trey[2], perim)
perim2 = perim
square2 = square
print("Сумма периметров треугольников:",perim1+perim2)
print("Сумма площадей треугольников:","%.3f"%(square1+square2))