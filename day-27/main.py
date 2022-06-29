import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

# Create the component
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))

# Specify how it will be layed out
my_label.pack(side="left")



# Makes the window persistent, has to be at the end
window.mainloop()