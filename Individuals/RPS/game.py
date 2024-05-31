import tkinter as tk
import random

# AI choice function
def get_ai_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Determine winner function
def determine_winner(player, ai):
    if player == ai:
        return "It's a tie!"
    elif (player == "rock" and ai == "scissors") or \
         (player == "scissors" and ai == "paper") or \
         (player == "paper" and ai == "rock"):
        return "You win!"
    else:
        return "AI wins!"

# Update result label function
def update_result(player_choice):
    ai_choice = get_ai_choice()
    player_choice_label.config(image=images[player_choice])
    ai_choice_label.config(image=images[ai_choice])
    result = determine_winner(player_choice, ai_choice)
    result_label.config(text=result)

# Main window setup
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Load icons
images = {
    "rock": tk.PhotoImage(file="rock.png").subsample(1),
    "paper": tk.PhotoImage(file="paper.png").subsample(1),
    "scissors": tk.PhotoImage(file="scissors.png").subsample(1),
    # Icon from icons8.com
    "human": tk.PhotoImage(file="human.png").subsample(1),
    "ai": tk.PhotoImage(file="ai.png").subsample(1)
}

# Result label
result_label = tk.Label(root, text="Choose Move:", font=("Helvetica", 25), pady=20)
result_label.pack()


# Frame for displaying choices
choices_frame = tk.Frame(root)
choices_frame.pack(pady=10)

# Player choice label
player_choice_label = tk.Label(choices_frame, image=images["human"], font=("Helvetica", 14))
player_choice_label.pack(side=tk.RIGHT, padx=20)

# AI choice label
ai_choice_label = tk.Label(choices_frame, image=images["ai"], font=("Helvetica", 14))
ai_choice_label.pack(side=tk.LEFT, padx=20)

# Buttons with text
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

rock_button = tk.Button(buttons_frame, text="Rock", command=lambda: update_result("rock"), font=("Helvetica", 14), width=10)
rock_button.pack(side=tk.LEFT, padx=10, pady=10)

paper_button = tk.Button(buttons_frame, text="Paper", command=lambda: update_result("paper"), font=("Helvetica", 14), width=10)
paper_button.pack(side=tk.LEFT, padx=10, pady=10)

scissors_button = tk.Button(buttons_frame, text="Scissors", command=lambda: update_result("scissors"), font=("Helvetica", 14), width=10)
scissors_button.pack(side=tk.LEFT, padx=10, pady=10)

# Run the GUI loop
root.mainloop()
