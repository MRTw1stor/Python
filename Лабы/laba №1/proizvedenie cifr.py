# Найдите произведение цифр заданного трёхзначного числа
abc = int(input("ВВедите трёхзначное число: "))
if abc > 99 and abc < 1000 :
    a = abc // 100
    b = abc // 10 % 10
    c = abc % 10
    print(a,"*",b,"*",c,"=",a*b*c)
else:
    print("Вы ввели не трёхзначное число")