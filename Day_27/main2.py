from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="I am a label", font=("Arial", 20, "bold"))
my_label.config(text="new text")
my_label.grid(column=0, row=0)

button = Button(text="click me")
button.grid(column=1, row=1)

new_button = Button(text="click me")
new_button.grid(column=2, row=0)

entry = Entry()
entry.grid(column=3, row=3)
window.mainloop()
