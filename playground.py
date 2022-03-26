from tkinter import *

NORMAL_FONT = ("Courier", 24, "normal")

window = Tk()
window.title("First GUI")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

def change_label_text():
    user_text = user_entry.get()
    my_label.config(text=user_text)


my_label = Label(text="Default Message", font=NORMAL_FONT)
my_label.grid(column=0, row=0)

my_button = Button(text="Click Me", font=("Courier", 10, "normal"), command=change_label_text)
my_button.grid(column=1, row=2)

button_2 = Button(text="Button 2", font=("Courier", 10, "normal"))
button_2.grid(column=3, row=0, )

user_entry = Entry(width=10)
user_entry.grid(column=1, row=1)


window.mainloop()
