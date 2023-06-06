class Computer:
    default_game = "Cards"

    def __init__(self, game):
        self.game = game
    # Метод объекта

    def play(self, start):
        if self.game == "Solitaire" and start == "ON":
            print(f"play {self.game}")
    # Статический метод

    @staticmethod
    def mouse(click):
        if click == "yes":
            return "click"
        elif click == "no":
            return "space"
        else:
            return None
    # Метод класса

    @classmethod
    def monitor(cls, game):
        monitor = cls(game)
        return monitor


computer_obj = Computer("Solitaire")
computer_obj.play("ON")
print(Computer.mouse("yes"))
print(Computer.monitor("miner"))
