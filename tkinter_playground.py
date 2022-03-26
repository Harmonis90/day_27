from tkinter import *

# Window Examples
window = Tk()
window.title("Play With My Buttons")
window.minsize(width=500, height=500)

# Label Examples
label_one = Label(text="Text Goes Here")
label_one.config(text="I am conscious!")
label_one.pack()

# Button Examples
def click_to_print():
    print("AI 'brain' erased.")

# calls on button down
button_one = Button(text="Click if sentient", command=click_to_print)
button_one.pack()


# Entries
entry_one = Entry(width=30)
# Add default text to entry
entry_one.insert(END, string="Add information to main brain...")
# Gets text in entry
print(entry_one.get())
entry_one.pack()

# Text
text = Text(width=30, height=5)
# Puts cursor in text box
text.focus()
# Add Default text
text.insert(END, "The AI can NOT see this text. Help!\n And do not touch anything!!")
# Gets current text at line 1 char index 0
print(text.get("1.0", END))
text.pack()

# Spinbox
def on_spinbox_use():
    # gets the current spinbox value
    print("AI calculating speed level. " + spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=on_spinbox_use)
spinbox.pack()

# Scale
# Called with current scale value
def scale_used(value):
    print(f"Capacity level {value}")


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def on_checkbutton_press():
    checked = checked_state.get()
    if checked:
        print("DOH")
    elif not checked:
        print("Good")
    else:
        print("Error")

# 1 if on else 0
checked_state = IntVar()
check_button = Checkbutton(text="If you played with the buttons ", variable=checked_state,
                           command=on_checkbutton_press)
checked_state.get()
check_button.pack()

def on_radiobutton_press():

    if radio_state.get() == 1:
        print("Fine. We can reverse the damage.")
    elif radio_state.get() == 2:
        print("50/50 we all die.")
    elif radio_state.get() == 3:
        print("You killed us all!")


radio_state = IntVar()
radio_button_one = Radiobutton(text="I only pressed a few buttons.", value=1,
                               variable=radio_state, command=on_radiobutton_press)
radio_button_two = Radiobutton(text="I may have fiddled a good amount.", value=2,
                               variable=radio_state, command=on_radiobutton_press)
radio_button_three = Radiobutton(text="I didn't listen. I played alot.", value=3,
                                 variable=radio_state, command=on_radiobutton_press)
radio_button_one.pack()
radio_button_two.pack()
radio_button_three.pack()


# Listbox
def on_listbox_used(event):
    if list_box.get(list_box.curselection()) == "Hero":
        print("You saved the world")
    elif list_box.get(list_box.curselection()) == "Demon":
        print("You came here to destroy!")
    elif list_box.get(list_box.curselection()) == "Sleep":
        print("Just a dream")
    elif list_box.get(list_box.curselection()) == "AI":
        print("An AI pretending to be human?")

list_box = Listbox(height=4)
player_options = ["Hero", "Demon", "Sleep", "AI"]
for i in player_options:
    list_box.insert(player_options.index(i), i)
list_box.bind("<<ListboxSelect>>", on_listbox_used)
list_box.pack()

window.mainloop()