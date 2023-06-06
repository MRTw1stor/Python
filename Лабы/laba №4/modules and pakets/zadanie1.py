from sys import path
# Импорт модуля calendar
import calendar
# Путь к библиотеки calendar
print(f"Путь к библиотеки calendar - {path[3]}\calendar.py")
print("")
# Список атрибутов модуля
print("Список атрибутов модуля calendar -",dir(calendar))
print("")
# Проверка 2027 год високосный или нет
if (calendar.isleap(2027)):
    print("2027 год - високосный")
else:
    print("2027 год - не високосный")
print("")
# Узнавание, каким днём недели является 25 июня 1995 года
print("25 июня 1995 года - ",calendar.weekday(1995, 6, 25),"день недели (понедельник - 0)")
print("")
# Календарь на 2023
country = calendar.LocaleTextCalendar(locale="ru")
country.pryear(2023)
