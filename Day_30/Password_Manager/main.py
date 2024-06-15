from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Function
def generate_password():
    # Define character sets for password generation
    letters = ['a', 'b', 'c', ..., 'Z']
    numbers = ['0', '1', '2', ..., '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate random characters
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine characters and shuffle to create a password
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Join list into a string and display in password entry field
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copy password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Retrieve user inputs
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Prepare new data dictionary
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Check if required fields are not empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            # Attempt to open existing data file
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # Create new data file if not found and write new_data
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update existing data with new_data
            data.update(new_data)
            # Write updated data back to file
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # Clear input fields after saving
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    # Retrieve website input
    website = website_entry.get()

    # Check if website field is empty
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please enter a website to search for.")
    else:
        try:
            # Attempt to open data file
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                if website in data:
                    # Display email and password for the website
                    email = data[website]["email"]
                    password = data[website]["password"]
                    messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
                else:
                    # Show message if website not found in data
                    messagebox.showinfo(title="Not Found", message=f"No details for {website} exists.")
        except FileNotFoundError:
            # Show error message if data file not found
            messagebox.showinfo(title="Error", message="No Data File Found.")
        except json.JSONDecodeError:
            # Show error message if data file is corrupted
            messagebox.showinfo(title="Error", message="Data file is corrupted.")

# ---------------------------- UI SETUP ------------------------------- #

# Initialize tkinter window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create canvas for logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels for UI elements
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry fields for user input
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=39)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons for actions
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Start the tkinter main loop
window.mainloop()