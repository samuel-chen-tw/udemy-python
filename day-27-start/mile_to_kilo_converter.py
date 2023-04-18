from tkinter import *


def calculate_miles():
    miles = float(input_miles.get())
    result = round(miles * 1.609)
    cover_label.config(text=f"{result}")


window = Tk()
window.title("Mile to Kilometers Converter")
window.minsize(width=250, height=100)

input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

cover_label = Label(text="0")
cover_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

covert_button = Button(text="Calculate", command=calculate_miles)
covert_button.grid(column=1, row=2)

window.mainloop()
