import tkinter as tk
from tkinter import font
import random
# Main class for the Guess the Number game
# It initializes the GUI, game stats, and manages the game logic

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
# Configure main window title, size, and make it non-resizable

        self.games_played = 0
        self.wins = 0
        self.losses = 0
# Initialize game statistics

        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=12)
        self.button_font = font.Font(family="Helvetica", size=12)
# Define fonts for title, labels, and buttons
    
        top_frame = tk.Frame(root, pady=10)
        top_frame.pack()
        self.info_label = tk.Label(top_frame, text="Guess a number between 1 and 100", font=self.title_font)
        self.info_label.pack()
        # Create frames for organizing widgets: top, middle, bottom
        # Top frame contains game instructions

        mid_frame = tk.Frame(root, pady=10)
        mid_frame.pack()
        self.entry = tk.Entry(mid_frame, font=self.label_font, width=10, justify='center')
        self.entry.grid(row=0, column=0, padx=5)
        self.submit_button = tk.Button(mid_frame, text="Submit Guess", font=self.button_font, command=self.check_guess, width=15)
        self.submit_button.grid(row=0, column=1, padx=5)
# Middle frame contains entry for user guess and submit button

        bottom_frame = tk.Frame(root, pady=10)
        bottom_frame.pack()
        self.feedback_label = tk.Label(bottom_frame, text="", font=self.label_font, fg="blue")
        self.feedback_label.pack()
        self.attempts_label = tk.Label(bottom_frame, text="", font=self.label_font)
        self.attempts_label.pack()
        self.stats_label = tk.Label(bottom_frame, text="", font=self.label_font)
        self.stats_label.pack()
# Bottom frame shows feedback, attempts left, and game stats

        self.restart_button = tk.Button(root, text="Restart Game", font=self.button_font, command=self.reset_game, width=20)
        self.restart_button.pack(pady=10)
# Restart button allows starting a new game

        self.reset_game()
# Initialize first game

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 5 + self.wins  # ۵ شانس پایه + تعداد بردها به عنوان شانس اضافه
        self.feedback_label.config(text="")
        self.entry.delete(0, tk.END)
        self.games_played += 1
        self.update_labels()
        self.submit_button.config(state=tk.NORMAL)
        self.info_label.config(text="Guess a number between 1 and 100")
# Reset the game state: choose new number, reset attempts, clear feedback, and update stats

    def update_labels(self):
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")
        self.stats_label.config(text=f"Games Played: {self.games_played} | Wins: {self.wins} | Losses: {self.losses}")
# Update labels showing attempts left and overall game statistics

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback_label.config(text="Please enter a valid number.", fg="red")
            return
        guess = int(guess)
        if guess < 1 or guess > 100:
            self.feedback_label.config(text="Number must be between 1 and 100.", fg="red")
            return

        self.attempts -= 1

        if guess == self.number_to_guess:
            self.wins += 1
            self.feedback_label.config(text=f"Correct! The number was {self.number_to_guess}. You won!", fg="green")
            self.end_game()
        elif guess < self.number_to_guess:
            self.feedback_label.config(text="Too low.", fg="orange")
        else:
            self.feedback_label.config(text="Too high.", fg="orange")

        self.update_labels()
        self.entry.delete(0, tk.END)

        if self.attempts <= 0:
            self.losses += 1
            self.feedback_label.config(text=f"Game Over! The number was {self.number_to_guess}. You lost!", fg="red")
            self.end_game()
# Process user's guess: validate input, compare with target number,
    # update attempts, wins/losses, and provide feedback

    def end_game(self):
        self.submit_button.config(state=tk.DISABLED)
        self.update_labels()
        self.info_label.config(text="Click 'Restart Game' to play again.")
 # Disable submit button and update labels when the game ends
    # Prompt user to restart the game

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
# Start the game: create main window and run the Tkinter event loop





