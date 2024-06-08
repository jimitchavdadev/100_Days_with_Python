from tkinter import *

window = Tk()
window.title("first GUI")
window.minsize(width=500, height=500)

# label
my_label = Label(text="I am a text", font=("arial", 24, "bold"))
my_label.pack()  # important to display the label

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    something = input.get()
    my_label.config(text=something)


button = Button(text="Click me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()


window.mainloop()
