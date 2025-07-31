from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Main window
window = Tk()
window.title("Rock Paper Scissor Game")
window.configure(background="black")


# images
user_rock = ImageTk.PhotoImage(Image.open("rock (1).png").resize((150, 150)))
user_paper = ImageTk.PhotoImage(Image.open("paper (1).png").resize((150, 150)))
user_scissor = ImageTk.PhotoImage(Image.open("scissor (1).png").resize((150, 150)))

comp_rock = ImageTk.PhotoImage(Image.open("rock (2).png").resize((150, 150)))
comp_paper = ImageTk.PhotoImage(Image.open("paper (2).png").resize((150, 150)))
comp_scissor = ImageTk.PhotoImage(Image.open("scissor (2).png").resize((150, 150)))



# image placeholders
user_label = Label(window, image=user_rock, bg="black")
user_label.grid(row=1, column=1)

comp_label = Label(window, image=comp_rock, bg="black")
comp_label.grid(row=1, column=3)



# Score labels
comp_score = Label(window, text="0", font=("Arial", 20), bg="black", fg="white")
comp_score.grid(row=0, column=3)

user_score = Label(window, text="0", font=("Arial", 20), bg="black", fg="white")
user_score.grid(row=0, column=1)



# Player indicators
user_indicator = Label(window, text="Player", font=("Arial", 15), bg="black", fg="white")
user_indicator.grid(row=2, column=1, pady=(10, 0))

comp_indicator = Label(window, text="Computer", font=("Arial", 15), bg="black", fg="white")
comp_indicator.grid(row=2, column=3, pady=(10, 0))



# Final result message
final_message = Label(window, font=("Arial", 16), bg="black", fg="white")
final_message.grid(row=4, column=2)




# Score update 
def updateMessage(msg):
    final_message['text'] = msg

def comp_update():
    final = int(comp_score['text'])
    final += 1
    comp_score['text'] = str(final)

def user_update():
    final = int(user_score['text'])
    final += 1
    user_score['text'] = str(final)



# Winner logic
def winner_check(user, comp):
    if user == comp:
        updateMessage("It's a Tie!")
    elif user == "rock":
        if comp == "paper":
            updateMessage("Computer Wins!")
            comp_update()
        else:
            updateMessage("Player Wins!")
            user_update()
    elif user == "paper":
        if comp == "scissor":
            updateMessage("Computer Wins!")
            comp_update()
        else:
            updateMessage("Player Wins!")
            user_update()
    elif user == "scissor":
        if comp == "rock":
            updateMessage("Computer Wins!")
            comp_update()
        else:
            updateMessage("Player Wins!")
            user_update()



# Choice logic
choices = ["rock", "paper", "scissor"]

def choice_update(user_choice):
    comp_choice = choices[randint(0, 2)]


    # Update images
    if comp_choice == "rock":
        comp_label.configure(image=comp_rock)
    elif comp_choice == "paper":
        comp_label.configure(image=comp_paper)
    else:
        comp_label.configure(image=comp_scissor)

    if user_choice == "rock":
        user_label.configure(image=user_rock)
    elif user_choice == "paper":
        user_label.configure(image=user_paper)
    else:
        user_label.configure(image=user_scissor)

    winner_check(user_choice, comp_choice)



# Buttons
button_rock = Button(window, width=16, height=3, text="Rock", command=lambda: choice_update("rock"))
button_rock.grid(row=5, column=1, padx=10, pady=10)

button_paper = Button(window, width=16, height=3, text="Paper", command=lambda: choice_update("paper"))
button_paper.grid(row=5, column=2, padx=10, pady=10)

button_scissor = Button(window, width=16, height=3, text="Scissor", command=lambda: choice_update("scissor"))
button_scissor.grid(row=5, column=3, padx=10, pady=10)



# Run 
window.mainloop()
