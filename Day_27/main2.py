from tkinter import *

# Create the main window
window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Create a label widget and configure its text
my_label = Label(text="I am a label", font=("Arial", 20, "bold"))
my_label.config(text="New Text")  # Change the label text
my_label.grid(column=0, row=0)  # Place the label in the window

# Create a button widget
button = Button(text="Click me")
button.grid(column=1, row=1)  # Place the button in the window

# Create another button widget
new_button = Button(text="Click me")
new_button.grid(column=2, row=0)  # Place the new button in the window

# Create an entry widget
entry = Entry()
entry.grid(column=3, row=3)  # Place the entry widget in the window

# Start the main event loop to display the window and handle user interactions
window.mainloop()