BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

from tkinter import *
from pandas import *
import random

try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = read_csv("data/french_words.csv")


to_learn = data.to_dict(orient="records")
#_________________________
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill ="black")
    canvas.itemconfig(card_image, image= card_front)
    flip_timer = window.after(3000, flip)

#_________________________
def flip():
    canvas.itemconfig(card_image, image= card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

#__________________________
def is_known():
    to_learn.remove(current_card)
    data = DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index= False)
    next_card()

# _________UI_____________

window = Tk()
window.title("Flash")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height= 526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 263, image= card_front)
card_title = canvas.create_text(400, 150, text="", font=("ariel", 48, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("ariel", 60, "bold"))
canvas.grid(column=0,row=0,columnspan=2)

righ_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=righ_image, highlightthickness=0, command=is_known)
right_button.grid(column=1,row=1)

wrong_button =Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0,row=1)

next_card()



window.mainloop()