import os
# Создаем файл
os.mkdir("pop.txt")
# Переименовываем файл
os.rename("pop.txt", "1-pop.txt")
# Удаляем файл
os.rmdir("1-pop.txt")
# Создаем каталог, если его нет
if not os.path.isdir("file"):
     os.mkdir("file")
print("Дерево нашего каталога:")
for dirpath, dirnames, filenames in os.walk("."):
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
    # перебрать файлы
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))
print("Размер файла renamed-pop.txt:",os.stat("renamed-pop.txt").st_size)
print("Текущая папка:",os.getcwd(),"\n","Все папки и файлы в текущем каталоге:",os.listdir())