print("Все четырёхзначные числа в которых нет одинаковых цифр")
for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                if (a != b) and if (a != c) and if (a != d) and if (b != c) and if (b != d) and if (c != d):
                    print(a,b,c,d)