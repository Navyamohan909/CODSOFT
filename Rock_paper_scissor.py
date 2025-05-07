import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game(user_choice):
    """Play a round of Rock-Paper-Scissors."""
    global user_score, computer_score

    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)

    if winner == "user":
        user_score += 1
        result = "You win!"
    elif winner == "computer":
        computer_score += 1
        result = "You lose!"
    else:
        result = "It's a tie!"

    result_label.config(text=f"Result: {result}")
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    score_label.config(text=f"Scores -> You: {user_score}, Computer: {computer_score}")

def reset_game():
    """Reset the game scores and UI."""
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Result: ")
    user_choice_label.config(text="Your Choice: ")
    computer_choice_label.config(text="Computer's Choice: ")
    score_label.config(text="Scores -> You: 0, Computer: 0")

# Initialize scores
user_score = 0
computer_score = 0

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x300")

# Add labels and buttons
tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 16)).pack(pady=10)

user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 12))
computer_choice_label.pack()

result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack()

score_label = tk.Label(root, text="Scores -> You: 0, Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Rock", font=("Arial", 12), command=lambda: play_game("rock")).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Paper", font=("Arial", 12), command=lambda: play_game("paper")).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Scissors", font=("Arial", 12), command=lambda: play_game("scissors")).grid(row=0, column=2, padx=10)

tk.Button(root, text="Reset", font=("Arial", 12), command=reset_game).pack(pady=10)
tk.Button(root, text="Quit", font=("Arial", 12), command=root.quit).pack()

# Run the main loop
root.mainloop()