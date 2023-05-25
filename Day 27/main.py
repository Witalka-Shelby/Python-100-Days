from tkinter import *
window = Tk()
window.title("Mil3 to Km Converter")
window.minsize(width=100, height=50)
window.config(padx=20, pady=20)

def convert_to_km():
    miles = float(user_input.get())
    kms = round(miles * 1.609, 2)
    label_converted.config(text=f"{kms}")


button = Button(text="Calculate", command=convert_to_km)
button.grid(column=1, row=2)

label1 = Label(text="is equal to")
label1.grid(column=0, row=1)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

user_input = Entry(width=10)
user_input.grid(column=1, row=0)

label_converted = Label(text="0")
label_converted.grid(column=1, row=1)

window.mainloop() 