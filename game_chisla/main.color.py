# Импортируем необходимые модули
from tkinter import *
import random
import tkinter as tk
import tkinter.ttk as ttk

class NumberGame(tk.Frame):

    # Настройки игры по умолчанию
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        self.difficulty_selected = False
        self.current_difficulty = "Легкий"
        self.difficulty_button_disabled = False
        self.create_widgets()

    # Создаем стили, кнопки и заголовок
    def create_widgets(self):

        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure('Custom.TButton', font=('Helvetica', 15), foreground='#7C7CFC', background='black', borderwidth=0, focusthickness=0, focuscolor='none')
        self.style.map('Custom.TButton', background=[('active','black')])
        self.style.configure('Custom.TLabel', font=('Helvetica', 40), foreground='#333', background='#F0F0F0')
        self.style.map('Custom.TLabel', background=[('active','#F0F0F0')])
        self.style.configure('Custom.TText', font=('Helvetica', 40), foreground='#333', background='#F0F0F0')
        self.style.map('Custom.TText', background=[('active','#F0F0F0')])

        self.difficulty_selected_label = ttk.Label(self, text="Текущий уровень сложности: " + self.current_difficulty, style='Custom.TLabel')
        self.difficulty_selected_label.pack(pady=(40, 10))

        self.difficulty_button = ttk.Button(self, text="Выбрать уровень сложности", command=self.show_difficulty_buttons, style='Custom.TButton', padding=15, width=25)
        self.difficulty_button.pack(pady=(10, 10))

        self.start_button = ttk.Button(text="Начать игру", command=self.start_countdown, style='Custom.TButton', padding=15, width=25)
        self.start_button.pack(pady=(0, 10))

        self.about_button = ttk.Button(text="Об игре", command=self.show_about, style='Custom.TButton', padding=15, width=25)
        self.about_button.pack(pady=(0, 10))

        self.quit_button = ttk.Button(text="Закрыть игру", command=self.master.destroy, style='Custom.TButton', padding=15, width=25)
        self.quit_button.pack(pady=(0, 340))

        self.button_frame = tk.Frame(self)

    # Делаем функционал кнопки "Об игре"
    # И добавляем краткое описание игры
    def show_about(self):
        self.difficulty_selected_label.pack_forget()
        self.difficulty_button.pack_forget()
        self.start_button.pack_forget()
        self.quit_button.pack_forget()
        self.about_button.pack_forget()

        self.about_label = tk.Text(self, wrap="word", width=120, height=15, font=('Helvetica', 20), foreground='#333', background='#F0F0F0', borderwidth=1)
        self.about_label.insert(tk.END, "Название игры: Сумма чисел\nЖанр: Логическая, Математическа игра\n\
Целевая аудитория: Игроки, которые хотят улучшить свои математические навыки и развить быстрое мышление.\n\
Цель игры: Развитие математических навыков, увеличение скорости вычислений и улучшение концентрации.\n\
Функционал: Игрок должен решать математические задачи, складывая числа, которые появляются на экране.\
 Игра состоит из нескольких уровней сложности, каждый из которых определяет скорость появления чисел, время отведенное на решение задачи и количество попыток ввода (жизней).\n\
Описание игры: Игра начинается с выбора уровня сложности. После выбора уровня, игроку предлагается сыграть один или несколько раундов, \
в каждом из которых нужно складывать числа, которые появляются на экране. После того как игрок посчитал сумму 10 чисел, ему предлагается ввести ответ на экране.\
 Если ответ правильный, игрок побеждает, если неправильный - у него остается определенное количество попыток, за которые ему нужно попробовать еще раз отгадать число.\
 Игра заканчивается, когда игрок вводит правильный ответ или когда у него заканчиваются попытки ввода.")
        self.about_label.configure(state="disabled")
        self.about_label.pack(pady=(40, 10))

        self.close_about_button = ttk.Button(self, text="Закрыть", command=self.close_about, style='Custom.TButton', padding=15, width=25)
        self.close_about_button.pack(pady=(400, 0))

    # Делаем функционал кнопки "Закрыть"
    def close_about(self):
        self.about_label.pack_forget()
        self.close_about_button.pack_forget()

        self.difficulty_selected_label.pack(pady=(40, 10))
        self.difficulty_button.pack(pady=(10, 10))
        self.start_button.pack(pady=(0, 10))
        self.about_button.pack(pady=(0, 10))
        self.quit_button.pack(pady=(0, 340))

    # Делаем функционал кнопки "Выбрать уровень сложности"
    # И создаем сами кнопки выбора уровня сложности
    def show_difficulty_buttons(self):
        if not self.difficulty_selected and not self.difficulty_button_disabled:

            self.easy_button = ttk.Button(self.button_frame, text="Легкий", command=lambda: self.set_difficulty("Легкий"), style='Custom.TButton', padding=10, width=15)
            self.easy_button.pack(side=tk.TOP, pady=5)

            self.medium_button = ttk.Button(self.button_frame, text="Средний", command=lambda: self.set_difficulty("Средний"), style='Custom.TButton', padding=10, width=15)
            self.medium_button.pack(side=tk.TOP, pady=5)

            self.hard_button = ttk.Button(self.button_frame, text="Сложный", command=lambda: self.set_difficulty("Сложный"), style='Custom.TButton', padding=10, width=15)
            self.hard_button.pack(side=tk.TOP, pady=5)

            self.imposible_button = ttk.Button(self.button_frame, text="Невозможный", command=lambda: self.set_difficulty("Невозможный"), style='Custom.TButton', padding=10, width=15)
            self.imposible_button.pack(side=tk.TOP, pady=5)

            self.button_frame.pack()
            self.difficulty_button_disabled = True
        else:
            self.easy_button.pack_forget()
            self.medium_button.pack_forget()
            self.hard_button.pack_forget()
            self.imposible_button.pack_forget()
            self.button_frame.pack_forget()
            self.difficulty_button_disabled = False

    # Устанавливаем время между появлением следующего числа для выбранного уровня сложности
    def get_delay(self):
        if self.current_difficulty == "Легкий":
            return 7
        elif self.current_difficulty == "Средний":
            return 5
        elif self.current_difficulty == "Сложный":
            return 3
        else:
            return 1
        
    # Устанавливаем количество попыток ввода(жизней) для выбранного уровня сложности
    def get_aptemps(self):
        if self.current_difficulty == "Легкий" or self.current_difficulty == "Средний":
            return 5
        else:
            return 3

    # Установка текущего уровня сложности
    def set_difficulty(self, difficulty):
        self.current_difficulty = difficulty
        self.difficulty_selected_label.configure(text="Текущий уровень сложности: " + difficulty)
        self.easy_button.pack_forget()
        self.medium_button.pack_forget()
        self.hard_button.pack_forget()
        self.imposible_button.pack_forget()
        self.difficulty_button_disabled = False

    # Запуск обратного отчета перед началом игры
    def start_countdown(self):
        self.start_button.pack_forget()
        self.difficulty_button.pack_forget()
        self.quit_button.pack_forget()
        self.about_button.pack_forget()
        self.difficulty_selected_label.pack_forget()
        self.countdown_label = tk.Label(self, font=("Helvetica", 300))
        self.countdown_label.pack(fill=tk.BOTH, expand=True)
        self.countdown(5)

    # Обновляет обратный отчет и запускате игру
    def countdown(self, remaining):
        if remaining <= 0:
            self.countdown_label.destroy()
            self.start_game()
        else:
            self.countdown_label.configure(text=str(remaining))
            self.after(1000, self.countdown, remaining-1)

    # Запуск игры
    def start_game(self):
        self.button_frame.pack_forget()
        self.number_label = tk.Label(self, font=("Helvetica", 200))
        self.number_label.pack(fill=tk.BOTH, expand=True)
        self.number_sum = 0
        self.numbers_shown = 0
        self.generate_numbers()
    # Создание случайных чисел в диапазоне от -25 до 25
    def generate_numbers(self):
        self.numbers_shown += 1
        if self.numbers_shown > 10:
            self.ask_sum()
        else:
            number = random.randint(-25, 25)
            self.number_sum += number
            self.number_label.configure(text=str(number))
            self.after(self.get_delay()*1000, self.generate_numbers)
            self.aptems = self.get_aptemps()

    # Создаем input для ввода суммы чисел
    # И спрашиваем сумму чисел у пользователя
    def ask_sum(self):
        self.number_label.destroy()

        self.answer_label = ttk.Label(self, text="Введите сумму:", style='Custom.TLabel')
        self.answer_label.pack(side=tk.TOP, pady=(30, 10))

        self.sum_entry = ttk.Entry(self, width=20, font=('Helvetica', 20))
        self.sum_entry.pack(pady=(400, 0))
        self.answer_entry = self.sum_entry
        self.answer_entry.bind("<Return>", self.check_sum)

        self.quit_button.pack_forget()

    # Проверка ответа пользователя
    def check_sum(self, event):
        print(self.number_sum)
        user_answer = int(self.answer_entry.get())
        if user_answer == self.number_sum:
            self.show_end_screen("Вы выиграли, поздравляем!")
        else:
            self.aptems = self.aptems - 1
            self.answer_entry.delete(0, tk.END)
            self.answer_label.configure(text="Неправильно, попробуйте еще раз :(\n\
Осталось попыток: {}".format(self.aptems))
            if (self.aptems == 0):
                self.show_end_screen("Вы проиграли, правильный ответ: {}".format(self.number_sum))

    # Экран окончания игры
    # Где создаются кнопки выйти в главное меню, сыграть снова и заголовок победили вы или проиграли
    def show_end_screen(self, message):
        self.end_game()

        self.message_label = ttk.Label(self, text=message, style='Custom.TLabel')
        self.message_label.pack(side=tk.TOP, pady=(30, 10))

        self.play_again_button = ttk.Button(self.button_frame, text="Сыграть снова", command=self.play_again, style='Custom.TButton', padding=15, width=25)
        self.play_again_button.pack(pady=(400, 10))

        self.quit_to_menu_button = ttk.Button(self.button_frame, text="Выйти в главное меню", command=self.quit_to_menu, style='Custom.TButton', padding=15, width=25)
        self.quit_to_menu_button.pack(pady=(5, 0))
        
        self.button_frame.pack()

    # Окончание игры
    def end_game(self):
        if hasattr(self, 'answer_label'):
            self.answer_label.destroy()
        if hasattr(self, 'answer_entry'):
            self.answer_entry.destroy()

    # Делаем функционал кнопки "Сыграть снова"
    def play_again(self):
        if hasattr(self, 'countdown_label'):
            self.countdown_label.destroy()
        elif hasattr(self, 'number_label'):
            self.number_label.destroy()
        self.message_label.destroy()
        self.play_again_button.destroy()
        self.quit_to_menu_button.destroy()
        self.difficulty_selected = False

        self.sum_entry = tk.Entry(self, width=20, font=("Helvetica", 20))
        self.start_countdown()
        self.button_frame.pack_forget()
        
    # Делаем функционал кнопки "Выйти в меню"
    def quit_to_menu(self):
        for widget in self.winfo_children():
            if widget != self.master:
                widget.destroy()
        self.create_widgets()
        self.button_frame.pack_forget()

# Запуск игры и открытие ее во весь экран
root = tk.Tk()
root.attributes("-fullscreen", True)
app = NumberGame(master=root)
app.mainloop()