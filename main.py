from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Main window
window = Tk()
window.title("Rock Paper Scissor Game")
window.configure(background="black")

# Load images
user_rock_img = ImageTk.PhotoImage(Image.open("rock (1).png").resize((150, 150)))
user_paper_img = ImageTk.PhotoImage(Image.open("paper (1).png").resize((150, 150)))
user_scissor_img = ImageTk.PhotoImage(Image.open("scissor (1).png").resize((150, 150)))

comp_rock_img = ImageTk.PhotoImage(Image.open("rock (2).png").resize((150, 150)))
comp_paper_img = ImageTk.PhotoImage(Image.open("paper (2).png").resize((150, 150)))
comp_scissor_img = ImageTk.PhotoImage(Image.open("scissor (2).png").resize((150, 150)))

# Display image placeholders
user_label = Label(window, image=user_rock_img, bg="black")
user_label.grid(row=1, column=1)

comp_label = Label(window, image=comp_rock_img, bg="black")
comp_label.grid(row=1, column=3)

# Score labels
comp_score = Label(window, text="0", font=("Arial", 20), bg="black", fg="white")
comp_score.grid(row=0, column=3)

user_score = Label(window, text="0", font=("Arial", 20), bg="black", fg="white")
user_score.grid(row=0, column=1)

# Player name indicators
user_indicator = Label(window, text="Player", font=("Arial", 15), bg="black", fg="white")
user_indicator.grid(row=2, column=1, pady=(10, 0))

comp_indicator = Label(window, text="Computer", font=("Arial", 15), bg="black", fg="white")
comp_indicator.grid(row=2, column=3, pady=(10, 0))

# Final message label
final_message = Label(window, text="", font=("Arial", 15), bg="black", fg="yellow")
final_message.grid(row=4, column=2)


def update_message(msg):
    final_message.config(text=msg)


def comp_update():
    score = int(comp_score['text'])
    score += 1
    comp_score.config(text=str(score))


def user_update():
    score = int(user_score['text'])
    score += 1
    user_score.config(text=str(score))


def winner_check(user, comp):
    if user == comp:
        update_message("It's a Tie!")
    elif user == "rock":
        if comp == "paper":
            update_message("Computer Wins!")
            comp_update()
        else:
            update_message("Player Wins!")
            user_update()
    elif user == "paper":
        if comp == "scissor":
            update_message("Computer Wins!")
            comp_update()
        else:
            update_message("Player Wins!")
            user_update()
    elif user == "scissor":
        if comp == "rock":
            update_message("Computer Wins!")
            comp_update()
        else:
            update_message("Player Wins!")
            user_update()


options = ["rock", "paper", "scissor"]


def choice_update(user_choice):
    comp_choice = options[randint(0, 2)]

    # Update user image
    if user_choice == "rock":
        user_label.config(image=user_rock_img)
    elif user_choice == "paper":
        user_label.config(image=user_paper_img)
    else:
        user_label.config(image=user_scissor_img)

    # Update computer image
    if comp_choice == "rock":
        comp_label.config(image=comp_rock_img)
    elif comp_choice == "paper":
        comp_label.config(image=comp_paper_img)
    else:
        comp_label.config(image=comp_scissor_img)

    # Check winner
    winner_check(user_choice, comp_choice)


def reset_game():
    user_label.config(image=user_rock_img)
    comp_label.config(image=comp_rock_img)
    user_score.config(text="0")
    comp_score.config(text="0")
    update_message("")


# Buttons
button_rock = Button(window, width=16, height=2, text="Rock", command=lambda: choice_update("rock"))
button_rock.grid(row=3, column=1, padx=10, pady=10)

button_paper = Button(window, width=16, height=2, text="Paper", command=lambda: choice_update("paper"))
button_paper.grid(row=3, column=2, padx=10, pady=10)

button_scissor = Button(window, width=16, height=2, text="Scissor", command=lambda: choice_update("scissor"))
button_scissor.grid(row=3, column=3, padx=10, pady=10)

# Restart button
reset_button = Button(window, width=16, height=2, text="Reset Game", bg="blue", fg="white", command=reset_game)
reset_button.grid(row=5, column=2, pady=15)

# Run GUI
window.mainloop()
