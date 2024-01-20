import tkinter as tk
import time
import random


def choose_random():
    num = random.randint(0, 2)
    if num == 0:
        return 'Rock'
    elif num == 1:
        return 'Paper'
    return 'Scissors'


class RPSGame:
    def __init__(self, score_counter, hand_seer):
        self.score_counter = score_counter
        self.tk_popup = tk.Tk()
        self.tk_popup.title('Goose')
        self.hand_seer = hand_seer

    def forfeit(self):
        self.score_counter.change_score(-10)
        self.tk_popup.quit()
        self.tk_popup.destroy()

    def play_rps(self):
        for widgets in self.tk_popup.winfo_children():
            widgets.destroy()

        count = 5

        scrollbar = tk.Scrollbar(self.tk_popup)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text = tk.Text(self.tk_popup, height=10, width=30, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        text.configure(font=("Comic Sans MS", 18))
        text.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=text.yview)
        text.insert(tk.END, "Show rock, paper, or scissors in:\n" + str(count) + "\n")
        self.tk_popup.update()

        for i in range(0, 5):
            time.sleep(1)
            count = count - 1
            text.insert(tk.END, str(count) + "\n")
            self.tk_popup.update()

        self.tk_popup.quit()
        self.tk_popup.destroy()

        hand_input = self.hand_seer.get_hand_gesture()

        self.tk_popup = tk.Tk()
        self.tk_popup.title('Goose')

        scrollbar = tk.Scrollbar(self.tk_popup)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text = tk.Text(self.tk_popup, height=10, width=30, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        text.configure(font=("Comic Sans MS", 18))
        text.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=text.yview)

        if hand_input == 'Closed_Fist':
            hand_input = 'Rock'

        elif hand_input == 'Open_Palm':
            hand_input = 'Paper'

        elif hand_input == 'Victory':
            hand_input = 'Scissors'

        goose_choice = choose_random()
        text.insert(tk.END, "The goose chose: " + goose_choice + "\n")
        text.insert(tk.END, "You chose: " + hand_input + "\n")
        if hand_input == goose_choice:
            text.insert(tk.END, "You tied! Nothing gained, nothing lost.\n")
        elif (hand_input == 'Rock' and goose_choice == 'Paper') or (hand_input == 'Scissors' and goose_choice == 'Rock')\
                or (hand_input == 'Paper' and goose_choice == 'Scissors'):
            self.score_counter.change_score(-15)
            text.insert(tk.END, "You lost! Lose 15 peas.\n")
        else:
            self.score_counter.change_score(15)
            text.insert(tk.END, "You Won! Gain 15 peas.\n")

        text.configure(state='disabled')
        tk.mainloop()

    def rock_paper_scissors_popup(self):
        """
        Display a popup for rock paper scissors
        Changes the score_counter depending on the outcome of the game
        """

        scrollbar = tk.Scrollbar(self.tk_popup)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text = tk.Text(self.tk_popup, height=10, width=30, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        text.configure(font=("Comic Sans MS", 18))
        text.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=text.yview)
        text.insert(tk.END, "A goose is demanding you to pay a toll to continue.\n")
        text.insert(tk.END, "You can pay 10 peas or challenge the goose to a game of rock, paper, scissors.\n")
        text.insert(tk.END, "If you win, the goose will give you 15 peas, but if you lose you have to pay 15 peas.\n")
        text.configure(state='disabled')

        pay_button = tk.Button(self.tk_popup, text='Pay up!', font=("Comic Sans MS", 18),
                               command=lambda: self.forfeit())
        pay_button.pack()
        play_button = tk.Button(self.tk_popup, text='Challenge!', font=("Comic Sans MS", 18),
                                command=lambda: self.play_rps())
        play_button.pack()
        tk.mainloop()
