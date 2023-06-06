spisok1 = [1,3,7,11,16,22,29,33]
spisok2 = ["Андрей","Миша","Витя","Гена","Денис","Настя","Маша","Ира","Надя"]
spisok3 = ['кошка','собака','лошадь','курица','дельфин','лев','попугай','зебра']
print("Список №1:",spisok1)
print("Список №2:",spisok2)
print("Список №3:",spisok3)
print("")
i = 0
while i < 1:
    print("Список действий:")
    print("Введите 1 чтобы добавить в список текстовый элемент")
    print("Введите 2 чтобы добавить в список числовой элемент")
    print("Введите 3 чтобы удалить из списка элемент")
    print("Введите 4 чтобы удалить весь список")
    print("Введите 5 чтобы объединить списки")
    a = input("Выберите действие:")
    if a == "1":
        x = 0
        while x < 1:
            w = input("Введите номер списка (1 или 2 или 3): ")
            if w == "1":
                print("Количество записей:",len(spisok1))
                print("Учитывайте что номер записи начинаеться с 0 ")
                d = int(input("Введите номер записи, перед которой добавить элемент"))
                spisok1.insert(d,input("Введите новый элемент"))
                print(spisok1)
            elif w =="2":
                print("Количество записей:",len(spisok2))
                print("Учитывайте что номер записи начинаеться с 0 ")
                d = int(input("Введите номер записи, перед которой добавить элемент"))
                spisok2.insert(d,input("Введите новый элемент"))
                print(spisok2)
            elif w == "3":
                print("Количество записей:",len(spisok3))
                print("Учитывайте что номер записи начинаеться с 0 ")
                d = int(input("Введите номер записи, перед которой добавить элемент"))
                spisok3.insert(d,input("Введите новый элемент"))
                print(spisok3)
            m = input("Добавить ещё элемент (да или нет)")
            if m != "да":
                x = x +1
    elif a == "2":
        x = 0
        while x < 1:
            w = input("Введите номер списка (1 или 2 или 3): ")
            if w == "1":
                print("Количество записей:",len(spisok1))
                print("Учитывайте что номер записи начинаеться с 0 ")
                d = int(input("Введите номер записи, перед которой добавить элемент"))
                spisok1.insert(d,float(input("Введите новый элемент")))
                print(spisok1)
            elif w =="2":
                print("Количество записей:",len(spisok2))
                print("Учитывайте что номер записи начинаеться с 0 ")
                d = int(input("Введите номер записи, перед которой добавить элемент"))
                spisok2.insert(d,float(input("Введите новый элемент")))
                print(spisok2)
            elif w == "3":
                print("Количество записей:",len(spisok3))
                print("Учитывайте что номер записи начинаеться с 0 ")
                d = int(input("Введите номер записи, перед которой добавить элемент"))
                spisok3.insert(d,float(input("Введите новый элемент")))
                print(spisok3)
            m = input("Добавить ещё элемент (да или нет)")
            if m != "да":
                x = x +1
    elif a == "3":
        x = 0
        while x < 1:
            w = input("Введите номер списка (1 или 2 или 3): ")
            if w == "1":
                print("Количество записей:",len(spisok1))
                print("Учитывайте что номер записи начинаеться с 0 ")
                d = int(input("Введите номер записи, которую хотите удалить"))
                spisok1.pop(d)
                print(spisok1)
            elif w =="2":
                print("Количество записей:",len(spisok2))
                print("Учитывайте что номер записи начинаеться с 0 ")
                d = int(input("Введите номер записи, которую хотите удалить"))
                spisok2.pop(d)
                print(spisok2)
            elif w == "3":
                print("Количество записей:",len(spisok3))
                print("Учитывайте что номер записи начинаеться с 0 ")
                d = int(input("Введите номер записи, которую хотите удалить"))
                spisok3.pop(d)
                print(spisok3)
            m = input("Удалить еще один елемент (да или нет)")
            if m != "да":
                x = x +1
    if a == "4":
        x = 0
        while x < 1:
            w = input("Введите номер списка (1 или 2 или 3): ")
            if w == "1":
                spisok1.clear()
                print(spisok1)
            elif w == "2":
                spisok2.clear()
                print(spisok2)
            elif w == "3":
                spisok3.clear()
                print(spisok3)
            m = input("Удалить еще один список (да или нет)")
            if m != "да":
                x = x +1
    if a == "5":
        x = 0
        while x < 1:
            w = input("Введите первый номер списка(1 или 2 или 3: ")
            q = input("Введите второй номер списка(1 или 2 или 3): ")
            if w == "1" and q == "2" or w == "2" and q == "1":
                spisok1.extend(spisok2)
                print(spisok1)
            elif w == "1" and q == "3" or w == "3" and q == "1":
                spisok1.extend(spisok3)
                print(spisok1)
            elif w == "2" and q == "3" or w == "3" and q == "2":
                spisok2.extend(spisok3)
                print(spisok2)
            elif w == "1" and q == "1":
                spisok1.extend(spisok1)
                print(spisok1)
            elif w == "2" and q == "2":
                spisok2.extend(spisok2)
                print(spisok2)
            elif w == "3" and q == "3":
                spisok3.extend(spisok3)
                print(spisok3)
            m = input("Объединить еще одну пару списков (да или нет)")
            if m != "да":
                x = x +1
    p = input("Вы хотете прозвести еще действие (да или нет)")
    if p != "да":
        i = i + 1
print("Измененный список №1:",spisok1)
print("Измененный список №2:",spisok2)
print("Измененный список №3:",spisok3)