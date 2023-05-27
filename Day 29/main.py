from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website_save = website_entry.get()
    username_save = username_entry.get()
    password_save = password_entry.get()

    
    with open("./day 29/data.txt", "a") as data_file:
        data_file.write("\n")
        data_file.write(f"{website_save}  |  {username_save}  |  {password_save}")

    website_entry.delete(0, END)
    password_entry.delete(0, END)


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

website_entry = Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()


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

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3, sticky="w")

###

add_button = Button(text="Add", width=43, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")


window.mainloop()