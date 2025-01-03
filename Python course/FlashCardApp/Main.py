from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
   data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    change_word()



def change_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=flash_front)
    canvas.itemconfig(title_txt, text="French", fill="black")
    canvas.itemconfig(word_txt, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(title_txt,text="English", fill="white")
    canvas.itemconfig(word_txt, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=flash_back)


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
flip_timer = window.after(3000, func=flip_card)
flash_front = PhotoImage(file="images/card_front.png")
flash_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=flash_front)
title_txt = canvas.create_text(400,150, fill="black", font=("Arial", 40, "italic"))
word_txt = canvas.create_text(400,263, fill="black", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
cross_img = PhotoImage(file="images/wrong.png")
Unknown_button = Button(image=cross_img, highlightthickness=0, command=change_word)
Unknown_button.grid(row=1,column=0)
check_img = PhotoImage(file="images/right.png")
yes_button = Button(image=check_img, highlightthickness=0, command=is_known)
yes_button.grid(row=1,column=1)
change_word()




window.mainloop()
