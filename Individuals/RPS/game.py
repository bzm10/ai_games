import tkinter as tk
import random
from PIL import Image, ImageTk

# Initialize scores
player_score = 0
ai_score = 0

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
        global player_score
        player_score += 1
        return "You win!"
    else:
        global ai_score
        ai_score += 1
        return "AI wins!"

# Update result label function
def update_result(player_choice):
    ai_choice = get_ai_choice()
    player_choice_label.config(image=player_images[player_choice])
    ai_choice_label.config(image=ai_images[ai_choice])
    result = determine_winner(player_choice, ai_choice)
    result_label.config(text=result)
    player_score_label.config(text=f"Player Score: {player_score}")
    ai_score_label.config(text=f"AI Score: {ai_score}")

# Rotate images for the player and AI
def rotate_image(image_path, angle):
    image = Image.open(image_path)
    rotated_image = image.rotate(angle, expand=True)
    return ImageTk.PhotoImage(rotated_image)

# Main window setup
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Load and rotate icons
player_images = {
    "rock": rotate_image("rock.png", 90),
    "paper": rotate_image("paper.png", 90),
    "scissors": rotate_image("scissors.png", 90),
    "human": rotate_image("human.png", 0)
}

ai_images = {
    "rock": rotate_image("rock.png", 270),
    "paper": rotate_image("paper.png", 270),
    "scissors": rotate_image("scissors.png", 270),
    "ai": rotate_image("ai.png", 0)
}

# Result label
result_label = tk.Label(root, text="Choose Move:", font=("Helvetica", 25), pady=20)
result_label.pack()

# Frame for displaying choices
choices_frame = tk.Frame(root)
choices_frame.pack(pady=10)

# Player choice label
player_choice_label = tk.Label(choices_frame, image=player_images["human"], font=("Helvetica", 14))
player_choice_label.pack(side=tk.RIGHT, padx=20)

# AI choice label
ai_choice_label = tk.Label(choices_frame, image=ai_images["ai"], font=("Helvetica", 14))
ai_choice_label.pack(side=tk.LEFT, padx=20)

# Frame for score labels
score_frame = tk.Frame(root)
score_frame.pack(pady=10)

# Player score label
player_score_label = tk.Label(score_frame, text=f"Player Score: {player_score}", font=("Helvetica", 14))
player_score_label.pack(side=tk.RIGHT, padx=65)

# AI score label
ai_score_label = tk.Label(score_frame, text=f"AI Score: {ai_score}", font=("Helvetica", 14))
ai_score_label.pack(side=tk.LEFT, padx=65)

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
