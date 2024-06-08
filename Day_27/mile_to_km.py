from tkinter import *


def convert():
    miles = 1.609 * float(entry.get())
    km_result.config(text=f"{miles}")


window = Tk()
window.title("miles to km converter")
window.minsize(width=400, height=100)
window.config(padx=20, pady=20)

entry = Entry(width=7)
entry.grid(column=1, row=0)

miles = Label(text=" Miles")
miles.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

km_result = Label()
km_result.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)

window.mainloop()
