import calendar
country = calendar.LocaleTextCalendar(locale="ru")
def yearF():
    global year
    n = 0
    while n != 1:
        year = int(input("Введите год: "))
        if 1 <= year <= 9999:
            n +=1
# Календарь на месяц
yearF()
q = 0
while q != 1:
    month = int(input("Введите месяц: "))
    if 1 <= month <= 12:
        q +=1
print(country.prmonth(year, month))
# Календарь на год
yearF()
print(country.pryear(year))