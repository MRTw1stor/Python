a = float(input("Введите число: "))
b = input("Введите символ артфметического действия {Пример: +, -, *, /}: ")
c = float(input("Введите число: "))
if b == "+":
    print(a,"+",c,"=","%.3f"%(a+c))
elif b == "-":
    print(a,"-",c,"=","%.3f"%(a-c))
elif b == "*":
    print(a,"*",c,"=","%.3f"%(a*c))
elif b == "/":
    if c == 0:
        print("На ноль делить нельзя")
    else:
        print(a,"/",c,"=","%.3f"%(a/c))
else:
    print("Неверный знак операции")