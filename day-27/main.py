from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

# Create the component
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))

# Specify how it will be layed out
my_label.grid(row=0, column=0)

# Change attributes of the label
my_label['text'] = "New text"
my_label.config(text="New text 2")

# Button

def button_on_click():
    print("I got clicked")
    my_label['text'] = input_field.get()

button = Button(text="Click me", command=button_on_click)
button.grid(row=1, column=1)

second_button = Button(text="New button")
second_button.grid(row=0, column=2)

# Entry

input_field = Entry(width=10)
input_field.grid(row=2, column=3)

# Makes the window persistent, has to be at the end
window.mainloop()