# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg

#     print(total)

# add(5, 8, 5, 2, 3, 6, 4 ,7, 7)

# def calculate(**kwargs):


from tkinter import *
window = Tk()
window.title("My first GUI App")
window.minsize(width=500, height=300)
window.config(padx=100, pady=120)

def button_click():
    new_label = user_input.get()
    my_label.config(text=new_label)

my_label = Label(text="MY LABEL")
my_label.grid(column=0, row=0)

button = Button(text="Click ME !!!", command=button_click)
button.grid(column=2, row=1)

button2 = Button(text="NEW BUTTON", command=button_click)
button2.grid(column=3, row=0)

user_input = Entry(width=20)
user_input.grid(column=4, row=3)

window.mainloop() 