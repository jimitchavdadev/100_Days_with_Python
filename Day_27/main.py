from tkinter import *

# Create the main window
window = Tk()
window.title("First GUI")
window.minsize(width=500, height=500)

# Create a label widget
my_label = Label(text="I am a text", font=("Arial", 24, "bold"))
my_label.pack()  # Display the label in the window

# Change the label text using dictionary-style assignment
my_label["text"] = "New Text"

# Change the label text using the config method
my_label.config(text="New Text")

# Define a function to be called when the button is clicked
def button_clicked():
    # Get the text from the entry widget
    something = input.get()
    # Update the label text with the text from the entry widget
    my_label.config(text=something)

# Create a button widget with a callback to the button_clicked function
button = Button(text="Click me", command=button_clicked)
button.pack()  # Display the button in the window

# Create an entry widget for user input
input = Entry(width=10)
input.pack()  # Display the entry widget in the window

# Start the main event loop to display the window and handle user interactions
window.mainloop()