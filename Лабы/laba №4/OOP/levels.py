class Computer:
    def __init__(self, game, application, program):
        # Public
        self.game = game
        # Protected
        self._application = application
        # Private
        self.__program = program


computer = Computer("Cards", "tik tok", "VS code")
# Вызов публичного атрибута
print(computer.game)
# Вызов защищенного атрибута
print(computer._application)
# Вызов приватного атрибута
print(computer._Computer__program)
