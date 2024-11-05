import random
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

class NumberGame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        self.difficulty_selected = False
        self.current_difficulty = "Легкий"
        self.difficulty_button_disabled = False
        self.create_widgets()

    def create_widgets(self):

        self.difficulty_selected_label = tk.Label(self,text="Текущий уровень сложности: " + self.current_difficulty)
        self.difficulty_selected_label.pack(pady=10)

        self.difficulty_button = ttk.Button(self,text="Выбрать уровень", command=self.show_difficulty_buttons)
        self.difficulty_button.pack(pady=10)

        self.start_button = ttk.Button(text="Начать игру", command=self.start_countdown)
        self.start_button.pack(pady=10)

        self.quit_button = ttk.Button(text="Закрыть игру", command=self.master.destroy)
        self.quit_button.pack(pady=10)

        self.button_frame = tk.Frame(self)
        

    def show_difficulty_buttons(self):
        if not self.difficulty_selected and not self.difficulty_button_disabled:
            self.easy_button = ttk.Button(self.button_frame, text="Легкий", command=lambda: self.set_difficulty("Легкий"))
            self.easy_button.pack(side=tk.TOP, pady=5)

            self.medium_button = ttk.Button(self.button_frame, text="Средний", command=lambda: self.set_difficulty("Средний"))
            self.medium_button.pack(side=tk.TOP, pady=5)

            self.hard_button = ttk.Button(self.button_frame, text="Сложный", command=lambda: self.set_difficulty("Сложный"))
            self.hard_button.pack(side=tk.TOP, pady=5)

            self.button_frame.pack()
            self.difficulty_button_disabled = True
        else:
            self.easy_button.pack_forget()
            self.medium_button.pack_forget()
            self.hard_button.pack_forget()
            self.button_frame.pack_forget()
            self.difficulty_button_disabled = False

    def set_difficulty(self, difficulty):
        self.current_difficulty = difficulty
        self.difficulty_selected_label.configure(text="Текущий уровня сложности: " + difficulty)
        self.easy_button.pack_forget()
        self.medium_button.pack_forget()
        self.hard_button.pack_forget()
        self.difficulty_button_disabled = False


    def start_countdown(self):
        self.start_button.pack_forget()
        self.difficulty_button.pack_forget()
        self.quit_button.pack_forget()
        self.difficulty_selected_label.pack_forget()
        self.countdown_label = tk.Label(self, font=("Helvetica", 36))
        self.countdown_label.pack(fill=tk.BOTH, expand=True)
        self.countdown(5)

    def countdown(self, remaining):
        if remaining <= 0:
            self.countdown_label.destroy()
            self.start_game()
        else:
            self.countdown_label.configure(text=str(remaining))
            self.after(1000, self.countdown, remaining-1)

    def start_game(self):

        self.button_frame.pack_forget()
        self.number_label= tk.Label(self, font=("Helvetica", 48))
        self.number_label.pack(fill=tk.BOTH, expand=True)
        self.number_sum = 0
        self.numbers_shown = 0
        self.generate_numbers()

    def generate_numbers(self):
        self.numbers_shown += 1
        if self.numbers_shown > 10:
            self.ask_sum()
        else:
            number = random.randint(-25, 25)
            self.number_sum += number
            self.number_label.configure(text=str(number))
            self.after(self.get_delay()*1000, self.generate_numbers)

    def get_delay(self):
        if self.current_difficulty == "Легкий":
            return 10
        elif self.current_difficulty == "Средний":
            return 5
        else:
            return 3

    def ask_sum(self):
        self.number_label.destroy()

        self.answer_label = tk.Label(self, text="Введите сумму:")
        self.answer_label.pack(side=tk.TOP, pady=10)

        self.answer_entry = tk.Entry(self, font=("Helvetica", 36))
        self.answer_entry.bind("<Return>", self.check_sum)
        self.answer_entry.pack(fill=tk.BOTH, expand=True)

        self.quit_button.pack_forget()

    def check_sum(self, event):
        user_answer = int(self.answer_entry.get())
        if user_answer == self.number_sum:
            self.show_end_screen("Правильно, поздравляем!")
        else:
            self.answer_entry.delete(0, tk.END)
            self.answer_label.configure(text="Неправильно, попробуйте еще раз :(")

    def show_end_screen(self, message):
        self.end_game()

        self.button_frame.pack(fill=tk.BOTH, expand=True)

        self.message_label = tk.Label(self, text=message, font=("Helvetica", 24))
        self.message_label.pack(fill=tk.BOTH, expand=True)

        self.play_again_button = tk.Button(self.button_frame, text="Сыграть снова", command=self.play_again)
        self.play_again_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.quit_to_menu_button = tk.Button(self.button_frame, text="Выйти в главное меню", command=self.quit_to_menu)
        self.quit_to_menu_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def end_game(self):
        self.answer_label.destroy()
        self.answer_entry.destroy()

    def play_again(self):
        if hasattr(self, 'countdown_label'):
            self.countdown_label.destroy()
        elif hasattr(self, 'number_label'):
            self.number_label.destroy()
        self.message_label.destroy()
        self.play_again_button.destroy()
        self.quit_to_menu_button.destroy()
        self.difficulty_selected = False
        self.start_countdown()

    def quit_to_menu(self):
        for widget in self.winfo_children():
            if widget != self.master:
                widget.destroy()
        self.create_widgets()

root = tk.Tk()
root.attributes("-fullscreen", True)
app = NumberGame(master=root)
app.mainloop()