class Computer:
    def __init__(self):
        self.game = "game"

    def info_computer(self):
        print(f'Class name: {Computer.__name__}')
        print(f'Name game: {self.game}')
# Унаследованный класс


class ServerComputer(Computer):
    def __init__(self):
        super().__init__()
        self.database = 0

    def info_computer(self):
        print(f'Class name: {ServerComputer.__name__}')
        print(f'Name game: {self.game}')
        print(f'Kol database: {self.database}')
# Работает для двух классов одновременно


def show_polymorphism():
    for item in [Computer, ServerComputer]:
        print('-------')
        object = item()
        object.info_computer()


show_polymorphism()
