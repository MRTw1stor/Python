grafic_otpuskov = {"январь":["Петрова А.С.","Киселев А.Д."],
                  "февраль":[],
                  "март":["Пахомов О.И.","Иванова О.О."],
                  "апрель":[],
                  "май":["Калинина В.М."],
                  "июнь":["Волкова М.С.","Павлов А.П."],
                  "июль":["Гончарова А.М.","Лаптев П.О."],
                  "август":["Соловьева Я.К."],
                  "сентябрь":[],
                  "октябрь":["Самойлов Д.М.","Смирнова Т.И."],
                  "ноябрь":["Нечаев М.Р."],
                  "декабрь":[]}
day = [3,10,15,13,14,20,29,5,24,7,1,18,11]
coll = 0
ind = -1
for key in grafic_otpuskov:
    coll = coll + len(grafic_otpuskov[key])
print("Всего сотрудников:",coll)
print("У всех вотрудников отпуск длиться 24 дня")
for key in grafic_otpuskov:
    for i in range(len(grafic_otpuskov[key])):
        ind = ind + 1
        print((ind + 1),")",grafic_otpuskov[key][i],"-",day[ind],key)
mount = input("Введите месяц отпуска:")
for key in grafic_otpuskov:
    if mount == key:
        print("Соотрудники у которых отпуск в",mount,":",grafic_otpuskov[mount])