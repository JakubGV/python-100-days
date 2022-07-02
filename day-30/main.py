from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
	try:
		with open('data.json', 'r') as f:
			data = json.load(f)
			website = website_input.get()
			login = data.get(website)
			message = ""
			
			if login is None:
				message = "Account not found"
			else:
				message = f"Email: {login['email']}\nPassword: {login['password']}"
			messagebox.showinfo(title=website, message=message)
	except FileNotFoundError:
		messagebox.showinfo(title="Oops", message="Could not open data.json")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_list = []
	password_list += [choice(letters) for _ in range(randint(8, 10))]
	password_list += [choice(symbols) for _ in range(randint(2, 4))]
	password_list += [choice(numbers) for _ in range(randint(2, 4))]

	shuffle(password_list)

	password = "".join(password_list)

	pass_input.insert(0, password)
	pyperclip.copy(password) # Copy the generated password to the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
	website = website_input.get()
	email = email_input.get()
	pswd = pass_input.get()
	new_data = {
        website: {
            'email': email,
            'password': pswd
        }
    }

	if len(website) == 0 or len(email) == 0 or len(pswd) == 0:
		messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
	else:
		try:
			with open('data.json', 'r') as f:
				data = json.load(f) # Read old data
		except FileNotFoundError:
			with open('data.json', 'w') as f:	
				json.dump(new_data, f, indent=4) # Save updated data
		else:
			data.update(new_data) # Update old with new data

			with open('data.json', 'w') as f:	
				json.dump(data, f, indent=4) # Save updated data
		finally:
			website_input.delete(0, END)
			pass_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=33)
website_input.focus()
website_input.grid(row=1, column=1)

search_btn = Button(text="Search", command=find_password, width=15)
search_btn.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input = Entry(width=52)
email_input.insert(0, "fake.email@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

pass_input = Entry(width=33)
pass_input.grid(row=3, column=1)

gen_pass_btn = Button(text="Generate Password", command=generate_password)
gen_pass_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()