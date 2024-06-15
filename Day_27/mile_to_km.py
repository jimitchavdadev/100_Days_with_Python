from tkinter import *

# Function to convert miles to kilometers
def convert():
    # Calculate kilometers from miles entered in the entry widget
    miles = 1.609 * float(entry.get())
    # Update the result label with the calculated kilometers
    km_result.config(text=f"{miles}")

# Create the main window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=100)
window.config(padx=20, pady=20)

# Create an entry widget for user input
entry = Entry(width=7)
entry.grid(column=1, row=0)  # Place the entry widget in the window

# Label "Miles" next to the entry widget
miles = Label(text=" Miles")
miles.grid(column=2, row=0)

# Label "is equal to" above the result
is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

# Result label for displaying the converted kilometers
km_result = Label()
km_result.grid(column=1, row=1)  # Place the result label in the window

# Label "Km" next to the result label
km = Label(text="Km")
km.grid(column=2, row=1)

# Button to trigger the conversion
calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)  # Place the button in the window

# Start the main event loop to display the window and handle user interactions
window.mainloop()