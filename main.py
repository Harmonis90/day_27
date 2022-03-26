from tkinter import *
FONT = ("Courier", 12, "normal")
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)

def convert_miles_km():
    mi = user_input.get()
    if mi.isdigit():
        kilo = int(mi) * 1.609
        km.set(f"{kilo:.2f}")

miles = IntVar()
user_input = Entry(width=10, textvariable=miles, justify="center")
user_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to", font=FONT)
equal_to_label.grid(column=0, row=1)


km = StringVar()
km_label = Label(text=f"0", font=FONT, textvariable=km)
km_label.grid(column=1, row=1)

km_text_label = Label(text="Km", font=FONT)
km_text_label.grid(column=2, row=1)

calc_button = Button(text="Calculate!", font=FONT, command=convert_miles_km)
calc_button.grid(column=1, row=2)










window.mainloop()