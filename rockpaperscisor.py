from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

# Main window setup
window = Tk()
window.title("Rock Paper Scissors Game")
window.geometry("420x450")
window.resizable(False, False)
big_font = ("Arial", 15, "bold")

# Labels
Label(window, text="Welcome to Rock Paper Scissors Game", font=big_font).pack(pady=10)
Label(window, text="Your Side", font=big_font).place(x=60, y=150)
Label(window, text="Computer", font=big_font).place(x=300, y=150)

# Load and resize images
try:
    rock_img = Image.open("rock.png").resize((60, 60))
    paper_img = Image.open("paper.webp").resize((60, 60))
    scissors_img = Image.open("scissors.png").resize((60, 60))

    rock_show = ImageTk.PhotoImage(rock_img)
    paper_show = ImageTk.PhotoImage(paper_img)
    scissors_show = ImageTk.PhotoImage(scissors_img)
except Exception as e:
    messagebox.showerror("Image Error", f"Could not load images: {e}")
    window.destroy()
    exit()

# Choices list
choices = ["rock", "paper", "scissors"]

# Labels to display images
player_label = Label(window)
computer_label = Label(window)
result_label = Label(window, font=big_font)

player_label.place(x=90, y=230)
computer_label.place(x=300, y=230)
result_label.place(x=160, y=320)

# Game logic
def play(player_choice):
    bot_choice = random.choice(choices)

    # Update images
    if player_choice == "rock":
        player_label.config(image=rock_show)
    elif player_choice == "paper":
        player_label.config(image=paper_show)
    elif player_choice == "scissors":
        player_label.config(image=scissors_show)

    if bot_choice == "rock":
        computer_label.config(image=rock_show)
    elif bot_choice == "paper":
        computer_label.config(image=paper_show)
    elif bot_choice == "scissors":
        computer_label.config(image=scissors_show)

    # Determine result
    if player_choice == bot_choice:
        result = "Draw"
    elif (player_choice == "rock" and bot_choice == "scissors") or \
         (player_choice == "paper" and bot_choice == "rock") or \
         (player_choice == "scissors" and bot_choice == "paper"):
        result = "You Win"
    else:
        result = "You Lose"

    result_label.config(text=result)

    # Save to log
    with open("game_log.txt", "a") as f:
        f.write(f"Player: {player_choice} | Computer: {bot_choice} | Result: {result}\n")

# Show log function
def show_log():
    if not os.path.exists("game_log.txt"):
        messagebox.showinfo("Game Log", "No games played yet!")
        return
    with open("game_log.txt", "r") as f:
        logs = f.read()
    messagebox.showinfo("Game Log", logs)

# Buttons for choices
button_frame = Frame(window)
button_frame.pack(pady=20)

Button(button_frame, text="Rock", font=big_font, width=10, command=lambda: play("rock")).grid(row=0, column=0, padx=5)
Button(button_frame, text="Paper", font=big_font, width=10, command=lambda: play("paper")).grid(row=0, column=1, padx=5)
Button(button_frame, text="Scissors", font=big_font, width=10, command=lambda: play("scissors")).grid(row=0, column=2, padx=5)

# Show log button
Button(window, text="Show Game Log", font=("Arial", 12), command=show_log).pack(pady=10)

# Run the main loop
window.mainloop()

