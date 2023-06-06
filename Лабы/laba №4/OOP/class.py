# Класс
class computer:
    # Переменная
    game = "cards"
    # Метод
    def play(self):
        pass

# Объект класса
computer_obj = computer()
# Список атрибутов
print(dir(computer_obj))
# Вызов из класса
print(computer_obj.game)
