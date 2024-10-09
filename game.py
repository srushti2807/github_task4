import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk
import winsound  # For sound effects (works only on Windows)
import os

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock-Paper-Scissors Game")
        master.geometry("500x600")
        master.config(bg="#282c34")

        self.user_score = 0
        self.computer_score = 0

        # Title
        self.title_label = tk.Label(master, text="Rock-Paper-Scissors", font=("Helvetica", 24, "bold"), bg="#282c34", fg="#61dafb")
        self.title_label.pack(pady=20)

        # Use relative path or current working directory
        base_path = os.getcwd()

        # Load images with the correct resampling method and path
        self.rock_image = ImageTk.PhotoImage(Image.open(os.path.join(base_path, "Downloads", "rock.png")).resize((100, 100), Image.Resampling.LANCZOS))
        self.paper_image = ImageTk.PhotoImage(Image.open(os.path.join(base_path, "Downloads", "paper.png")).resize((100, 100), Image.Resampling.LANCZOS))
        self.scissors_image = ImageTk.PhotoImage(Image.open(os.path.join(base_path, "Downloads", "scissors.png")).resize((100, 100), Image.Resampling.LANCZOS))

        # User choice buttons
        self.rock_button = tk.Button(master, image=self.rock_image, command=lambda: self.play("rock"), bg="#61dafb", borderwidth=0)
        self.paper_button = tk.Button(master, image=self.paper_image, command=lambda: self.play("paper"), bg="#61dafb", borderwidth=0)
        self.scissors_button = tk.Button(master, image=self.scissors_image, command=lambda: self.play("scissors"), bg="#61dafb", borderwidth=0)

        self.rock_button.pack(pady=10)
        self.paper_button.pack(pady=10)
        self.scissors_button.pack(pady=10)

        # Result display
        self.result_label = tk.Label(master, text="", font=("Helvetica", 18), bg="#282c34", fg="#ffffff")
        self.result_label.pack(pady=20)

        # Score display
        self.score_label = tk.Label(master, text="Score - You: 0  Computer: 0", font=("Helvetica", 16), bg="#282c34", fg="#ffffff")
        self.score_label.pack(pady=10)

        # Play again button
        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_game, bg="#ffca28", fg="black", width=15)
        self.play_again_button.pack(pady=20)

        self.play_again_button.config(state=tk.DISABLED)

        # Add sound effects
        self.win_sound = "win.wav"  # Replace with actual path to your sound file
        self.lose_sound = "lose.wav"  # Replace with actual path to your sound file
        self.tie_sound = "tie.wav"  # Replace with actual path to your sound file

    def play(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        self.display_choices(user_choice, computer_choice)
        winner = self.determine_winner(user_choice, computer_choice)
        self.update_score(winner)
        self.play_sound(winner)

    def display_choices(self, user_choice, computer_choice):
        self.result_label.config(text=f"You chose: {user_choice.capitalize()}\nComputer chose: {computer_choice.capitalize()}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "user"
        else:
            return "computer"

    def update_score(self, winner):
        if winner == "user":
            self.user_score += 1
            self.result_label.config(text=self.result_label.cget("text") + "\nYou Win!")
        elif winner == "computer":
            self.computer_score += 1
            self.result_label.config(text=self.result_label.cget("text") + "\nYou Lose!")
        else:
            self.result_label.config(text=self.result_label.cget("text") + "\nIt's a Tie!")

        self.score_label.config(text=f"Score - You: {self.user_score}  Computer: {self.computer_score}")
        self.play_again_button.config(state=tk.NORMAL)

    def play_sound(self, winner):
        if winner == "user":
            winsound.PlaySound(self.win_sound, winsound.SND_FILENAME)
        elif winner == "computer":
            winsound.PlaySound(self.lose_sound, winsound.SND_FILENAME)
        else:
            winsound.PlaySound(self.tie_sound, winsound.SND_FILENAME)

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score - You: 0  Computer: 0")
        self.result_label.config(text="")
        self.play_again_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
