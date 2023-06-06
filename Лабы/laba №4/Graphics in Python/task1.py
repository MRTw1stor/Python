from tkinter import *
from random import *
from time import *
# Окно
window = Tk()
# Название
window.title("Задание №1")
# Ширина и высота окна
size = 700
# Создание холста
canvas = Canvas(window, width=size, height=size)
canvas.pack()
# Массив цветов, которые используются
colorArray = ["red", "blue", "black", "green", "aqua", "purple", "fuchsia",
              "maroon", "orange", "pink", "yellow", "violet", "indigo", "chartreuse", "lime"]
while True:
    # Рандомный выбор цвета
    color = colorArray[round(random()*(len(colorArray)-1))]
    xyz = []
    for i in range(10):
        # Рандомные точки координат
        xyz.append(randint(0, size))
    # Рандомная фигура
    num = round(random()*4)
    if (num == 0):
        # Создать круг
        canvas.create_oval(xyz[0], xyz[1], xyz[2], xyz[3], fill=color)
    elif (num == 1):
        # Создать квадрат
        canvas.create_rectangle(xyz[0], xyz[1], xyz[2], xyz[3], fill=color)
    elif (num == 2):
        # Создать треугольник
        canvas.create_polygon(xyz[0], xyz[1], xyz[2],
                              xyz[3], xyz[4], xyz[5], fill=color)
    elif (num == 3):
        # Создание линии
        canvas.create_line(xyz[0], xyz[1], xyz[2], xyz[3], fill=color, width=2)
    elif (num == 4):
        # Создать пятиугольника
        canvas.create_polygon(xyz[0], xyz[1], xyz[2],
                              xyz[3], xyz[4], xyz[5], xyz[6], xyz[7], xyz[8], xyz[9], fill=color)
    # Обновить окно
    window.update()
    # Задержка на 0.1 секунды
    sleep(0.1)
