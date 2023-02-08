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
# функция нахождения периметра треугольника
perim = 0
def P():
    global perim
    perim = 0
    for j in range(3):
        perim = perim + trey[j]
# функция нахождения площади треугольника
square = 0
def S():
    global square
    square = 0
    semiperim = perim/2
    square =(semiperim *(semiperim-trey[0])*(semiperim-trey[1])*(semiperim-trey[2])) ** (0.5)
# вызов функций для нахождения значений
print("Введите стоноры первого треугольника")
treugolnik()
P()
S()
perim1 = perim
square1 = square
print("Введите стоноры второго треугольника")
treugolnik()
P()
S()
perim2 = perim
square2 = square
print("Сумма периметров треугольников:",perim1+perim2)
print("Сумма площадей треугольников:","%.3f"%(square1+square2))
