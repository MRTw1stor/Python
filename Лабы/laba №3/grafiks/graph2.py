from tkinter import *
from math import *
from random import *


def createText(place, text):  # Функция создания текста
    # Создание текста
    lbl = Label(place)
    # Название текста
    lbl["text"] = text
    # Отображение текста в левой части меню
    lbl.pack({"side": "left"})


def createShaft(startX, startY, endX, endY):  # Функция создания оси
    axe = []
    xy = (startX, startY)
    axe.append(xy)
    xy = (endX, endY)
    axe.append(xy)
    canvas.create_line(axe, fill="black", width=2)


def callbackColor(*args):  # Функция изменения цвета функции
    canvas.itemconfig(line, fill=variableColor.get())


def callbackThickness(*args):  # Функция изменения толщины функции
    canvas.itemconfig(line, width=variableThickness.get())


def createOptionList(place, variable, arrayValues, function):
    # Значение по умолчанию
    variable.set(arrayValues[0])
    # Создание всплывающего списка
    List = OptionMenu(place, variable, *arrayValues)
    # Добавление всплывающего списка в левую часть меню
    List.pack({"side": "left"})
    # Вызов изменения функции
    variable.trace("w", function)


# Создание окна
tk = Tk()
# Название
tk.title("Графика")
# Создание меню
menuFrame = Frame()
# Отображение меню в вверху
menuFrame.pack({"side": "top", "fill": "x"})
# Создание заголовка
createText(menuFrame, "Меню:")
# Создание заголовка выбора цвета
createText(menuFrame, "Выбор цвета:")
# Массив с цветами, которые можно выбрать для функции
color = ["black", "red", "blue", "green", "aqua", "purple", "fuchsia",
         "maroon", "orange", "pink", "yellow", "violet", "indigo", "chartreuse", "lime"]
# Создание значения по умолчанию
variableColor = StringVar(tk)
# Создание всплывающего списка цветов
createOptionList(menuFrame, variableColor, color, callbackColor)
# Создание заголовка выбора толщины
createText(menuFrame, "Выбор толщины:")
# Массив с толщиной, которую можно выбрать для функции
thickness = []
for i in range(1, 11):
    thickness.append(i)
# Создание значения по умолчанию
variableThickness = StringVar(tk)
# Создание всплывающего списка толщины
createOptionList(menuFrame, variableThickness, thickness, callbackThickness)
# Массив значений функции
points = [[], [], [], []]
# Высота функции
ay = 150
# Высота оси y
y0 = 150
# Начало оси x
x0 = 50
# Конец оси x
x1 = 470
# Шаг функции
dx = 10
# Вычисление графика функции
for i in range(4):
    for n in range(x0, x1, 5):
        arrayFunctions = [
            y0-ay*cos(n*dx), y0+ay*sin(n*dx), y0+ay/2*tan(n*dx), y0+ay/2*tan(n*dx)*(-1)]
        y = arrayFunctions[i]
        pp = (n, y)
        points[i].append(pp)
# Создание кнопки
but = Button(menuFrame)
# Название кнопки
but["text"] = "Закрыть"
# Команда, срабатывающая при нажатии на кнопку
but["command"] = tk.quit
# Добавляем кнопку в левую часть меню
but.pack({"side": "right"})
# Создание холста
canvas = Canvas(tk)
size = 120
canvas["height"] = size*3
canvas["width"] = size*4
# Цвет заднего фона
canvas["background"] = "white"
# Ширина бортиков
canvas["borderwidth"] = 2
# Добавление холста в окно
canvas.pack()
# Добавление графика функции
line = canvas.create_line(points[randint(0, 3)], fill=variableColor.get(),
                          smooth=1, width=variableThickness.get())
# Ось y на графике
createShaft(x0, 0, x0, y0+ay)
# Ось x на графике
createShaft(x0, y0, x1, y0)
# Добавление осей координат
xLine = x0-10
yLine = ((y0+ay)/2)
canvas.create_text(xLine, 10, text="y")
canvas.create_text(xLine, yLine, text="0,0")
canvas.create_text(x1, yLine-10, text="x")
# Конец
tk.mainloop()

