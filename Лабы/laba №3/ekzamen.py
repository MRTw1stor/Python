print("Студенты которые успешно сдали все экзамены: ")
print()
with open('students.txt','r',encoding="utf-8")as spis:
    print (spis.readline())
    for line in spis:
        while True:
            stud = spis.readline()
            if not stud:break 
            ball1 = int(stud.split()[1])
            ball2 = int(stud.split()[2])
            ball3 = int(stud.split()[3])
            if ball1 >= 3 and ball2 >= 3 and ball3 >= 3:
                print(stud)
        print()