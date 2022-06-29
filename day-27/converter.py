from tkinter import *

# Initialize window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)

# Left section
equal_to = Label(text="is equal to")
equal_to.grid(row=1, column=0)

# Middle section
miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

km_result = Label(text="0")
km_result.grid(row=1, column=1)


def convert_mi_to_km():
    miles_in = float(miles_input.get())
    km_result['text'] = str(miles_in * 1.609)

calc_btn = Button(text="Calculate", command=convert_mi_to_km)
calc_btn.grid(row=2, column=1)

# Right section
miles = Label(text="Miles")
miles.grid(row=0, column=2)

km = Label(text="Km")
km.grid(row=1, column=2)

window.mainloop()