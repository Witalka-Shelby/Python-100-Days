import tkinter

window = tkinter.Tk()
window.title("My first GUI App")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="MY LABEL")
my_label.pack()




window.mainloop()