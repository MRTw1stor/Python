class Computer:
    # Статическое поле
    default_game = "Cards"

    def __init__(self, game):
        # Динамическое поле
        self.game = game


computer_obj = Computer("Solitaire")
print(computer_obj.default_game)
print(computer_obj.game)
