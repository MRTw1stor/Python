rightAnswers = []
userAnswers = []
countRightAnswers = 0

# Открытие файла с тестом
with open('Questions.txt','r', encoding='utf-8') as Questions:
    answers = Questions.readlines()
# Запись правильных ответов
    a = answers[1]
    rightAnswers = a.split(", ")
    
    for q in range(5):
        rightAnswers[q] = int(rightAnswers[q])
# Прохождение теста
    for j in range(5):
        for i in range(4):
            print(answers[i+3+(j*5)])
        otvet = int(input("выберите вариант ответа: "))
        userAnswers.append(otvet)

        if userAnswers[j] == rightAnswers[j]:
            print()
            countRightAnswers +=1
        else:
            print()
# Вывод
    print("Ваши ответы:      ",userAnswers)
    print("Правильные ответы:",rightAnswers, '\n')
    if countRightAnswers < 3:
        print("Ваша оценка: 2")
    elif countRightAnswers == 3:
        print("Ваша оценка: 3")
    elif countRightAnswers == 4:
        print("Ваша оценка: 4")
    else:
        print("Ваша оценка: 5")