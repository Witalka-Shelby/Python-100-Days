from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pwd():
    pwd = []
    for _ in range(random.randint(14, 24)):
        pwd.append(random.choice((random.choice(string.ascii_letters), random.choice(string.punctuation), random.choice(string.digits))))

    password_entry.delete(0, END)
    password_entry.insert(0, f"{''.join(pwd)}")
    pyperclip.copy(''.join(pwd))

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website_save = website_entry.get()
    username_save = username_entry.get()
    password_save = password_entry.get()
    json_data = {website_save.lower(): {
        "email": username_save,
        "password": password_save
    }}

    if len(website_save) == 0 or len(username_save) == 0 or len(password_save) == 0:
        messagebox.showinfo(title="Info", message="No empty fields allowed !!")

    else:
        try:
            with open("./day 29/data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(json_data)

            with open("./day 29/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        except FileNotFoundError:
            with open("./day 29/data.json", "w") as data_file:
                json.dump(json_data, data_file, indent=4)
                
        finally:
            # clear entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    search_text = website_entry.get()
    search_text = search_text.lower()

    if len(search_text) == 0:
        messagebox.showinfo(title="Info", message="Search box is empty !!")

    else:
        try:
            with open("./day 29/data.json", "r") as find_accounts:
                accounts_list_json = json.load(find_accounts)
                if search_text in accounts_list_json:
                    username = accounts_list_json[search_text]["email"]
                    password = accounts_list_json[search_text]["password"]
                    messagebox.showinfo(title=f"{search_text}'s Login", message=f"Username: {username}\nPassword: {password}")
                else:
                    messagebox.showinfo(title="Error", message=f"No details for the {search_text} exists")

        except FileNotFoundError:
            messagebox.showerror(title="Error", message="Do Data File Found")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("P455WORD")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(height=200, width=200, highlightthickness=0)
logo_png = PhotoImage(file="./day 29/logo.png")
canvas.create_image(100, 95, image=logo_png)
canvas.grid(column=1, row=0)

#Website
website_label = Label(text="Website:", highlightthickness=0)
website_label.grid(column=0, row=1, sticky="e")

website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

search_button = Button(text="Search", command=find_password, width=14)
search_button.grid(column=2, row=1, sticky="w")


# Email/Username
username_label = Label(text="Email / Username:", highlightthickness=0)
username_label.grid(column=0, row=2, sticky="e")

username_entry = Entry(width=51)
username_entry.insert(0, "test@test.com")
username_entry.grid(column=1, row=2, columnspan=2, sticky="w")

#Pasword
password_label = Label(text="Password:", highlightthickness=0)
password_label.grid(column=0, row=3, sticky="e")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="w")

generate_button = Button(text="Generate Password", command=generate_pwd)
generate_button.grid(column=2, row=3, sticky="w")

###

add_button = Button(text="Add", width=43, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")


window.mainloop()