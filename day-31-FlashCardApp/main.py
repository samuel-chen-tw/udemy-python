from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
new_word = {}
data_list = {}

# use pandas to get the data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_list = original_data.to_dict(orient="records", )
else:
    data_list = data.to_dict(orient="records")



def know_the_word():
    data_list.remove(new_word)
    new_data = pandas.DataFrame(data_list)
    new_data.to_csv("data/words_to_learn.csv", index=False)

    change_word()


def change_word():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(data_list)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_word, text=new_word["French"], fill="Black")

    flip_timer = window.after(3000, func=change_to_english)


def change_to_english():
    global new_word
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=new_word["English"], fill="White")


# init window
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

flip_timer = window.after(3000, func=change_to_english)

# image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", fill="Black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", fill="Black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=know_the_word)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=change_word)
wrong_button.grid(column=0, row=1)

change_word()

window.mainloop()
