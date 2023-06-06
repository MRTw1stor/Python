class MyError(Exception):
    print("Моя проблема")
i = 0
while i < 5:
    try:
        if i == 0:
            print(1/0)
        elif i == 1:
            print('1'+1)
        elif i == 2:
            print(abc)
        elif i == 3:
            x = float("drgfew")
        elif i == 4:
            raise MyError("Вызов своей ошибки")
    except TypeError:
        print("Вы сложили значения несовместимых типов")
    except ZeroDivisionError:
        print("Деление на ноль")
    except NameError:
        print("Переменная не существует")
    except ValueError:
        print("Это ошибка значения")
    except MyError:
        print("Поймали свою ошибку")
    except:
        print("Что-то пошло не так...")
    finally:
        i = i + 1 