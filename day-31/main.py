from tkinter import *
import pandas as pd
import random
import os
BACKGROUND_COLOR = "#B1DDC6"

flip_timer = None
word_pair = None

# ---------------------------- CARD CHANGING LOGIC ------------------------------- #
def next_card():
    global flip_timer, word_pair
    if flip_timer is not None:
        window.after_cancel(flip_timer)

    word_pair = random.choice(words_to_learn)
    
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(title_text, text="Czech", fill="black")
    canvas.itemconfig(word_text, text=word_pair['Czech'], fill="black")

    flip_timer = window.after(3000, flip_card)

def flip_card():
    global word_pair
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word_pair['English'], fill="white")

def remove_card():
    global word_pair, words_to_learn
    words_to_learn.remove(word_pair)
    words_to_learn_df = pd.DataFrame(words_to_learn)
    words_to_learn_df.to_csv('data/words_to_learn.csv', index=False)
    next_card()

# ---------------------------- READ WORD LIST ------------------------------- #
if os.path.exists('data/words_to_learn.csv'):
    czech_words_df = pd.read_csv('data/words_to_learn.csv')
else:
    czech_words_df = pd.read_csv('data/czech_words.csv')

words_to_learn = czech_words_df.to_dict(orient="records")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

no_img = PhotoImage(file="images/wrong.png")
no_btn = Button(image=no_img, command=next_card, highlightthickness=0)

yes_img = PhotoImage(file="images/right.png")
yes_btn = Button(image=yes_img, command=remove_card, highlightthickness=0)

canvas.grid(row=0, column=0, columnspan=2)
no_btn.grid(row=1, column=0)
yes_btn.grid(row=1, column=1)

next_card()

window.mainloop()