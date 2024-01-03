from tkinter import *
from tkinter import messagebox
import pyperclip
import json

import random


def password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_number = [random.choice(symbols) for _ in range(nr_symbols)]
    password_symbols = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbols + password_number

    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    p_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    web = web_e.get()
    email = e_entry.get()
    password = p_entry.get()

    new_data = {
        web: {
            "email": email,
            "password": password,

        }
    }

    if len(web) == 0:
        messagebox.showinfo(title="info", message="Website field is empty")

    elif len(email) == 0:
        messagebox.showinfo(title="Information", message="email field is empty")

    elif len(password) == 0:
        messagebox.showinfo(title="Information", message="Password field is empty")
    else:
        try:

            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:

            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_e.delete(0, END)
            e_entry.delete(0, END)
            p_entry.delete(0, END)


def find_password():
    web = web_e.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Not Found", message="This file does not exist")

    else:

        if web in data:
            email = data[web]["email"]
            password = data[web]["password"]

            messagebox.showinfo(title=web, message=f"Email:{email}\n Password:{password}")

        else:
            messagebox.showinfo(title="Oops" , message="This website does not exist in the data ")


window = Tk()

window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

Email_label = Label(text="Email/Username")
Email_label.grid(row=2, column=0)

ps = Label(text="Password")
ps.grid(row=3, column=0)

web_e = Entry(width=35)
web_e.grid(row=1, column=1, columnspan=2)
web_e.focus()

e_entry = Entry(width=35)
e_entry.grid(row=2, column=1, columnspan=2)
e_entry.insert(0, "raj@gmail.com")

p_entry = Entry(width=21)
p_entry.grid(row=3, column=1)

search_button = Button(text="Search", command=find_password)

search_button.grid(row=1, column=3)

gen_button = Button(text="Generate", command=password)
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1)

window.mainloop()
