from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# Converted CSV file data into a python dictionary.
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')
    word_list = data.to_dict(orient='records')
else:
    word_list = data.to_dict(orient='records')
current_word = {}


def new_card():
    global current_word, flip_timer
    win.after_cancel(flip_timer)
    current_word = random.choice(word_list)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_word['French'], fill='black')
    canvas.itemconfig(back_ground, image=card_front_image)
    flip_timer = win.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_word['English'], fill='white')
    canvas.itemconfig(back_ground, image=card_background_image)


def is_known():
    word_list.remove(current_word)
    new_data = pd.DataFrame(word_list)
    new_data.to_csv('data/words_to_learn.csv')
    new_card()


win = Tk()
win.title('Flashy')
win.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = win.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file='images/card_front.png')
card_background_image = PhotoImage(file='images/card_back.png')
back_ground = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 132, text='Title', font=('arial', 40, 'normal'))
card_word = canvas.create_text(400, 263, text='word', font=('arial', 40, 'normal'))
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
wrong = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=wrong, command=new_card)
unknown_button.grid(row=1, column=0)
right = PhotoImage(file='images/right.png')
known_button = Button(image=right, command=is_known)
known_button.grid(row=1, column=1)

new_card()

win.mainloop()
