class Computer:
    def __init__(self):
        self.game = "game"
# Унаследованный класс


class ServerComputer(Computer):
    # Добавление нового атрибута
    def __init__(self):
        super().__init__()
        self.database = 0

    def plus_database(self, database):
        self.database = database+1
        print(f"На сервере {self.database} баз данных")


my_server_computer = ServerComputer()
# Унаследованный атрибут
print(my_server_computer.game)
# Новый метод
my_server_computer.plus_database(11)
