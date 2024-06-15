from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# Function to generate a random password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Create a password list with random characters
    password_list = [choice(letters) for _ in range(randint(8, 10))]  # Random letters
    password_list += [choice(symbols) for _ in range(randint(2, 4))]  # Random symbols
    password_list += [choice(numbers) for _ in range(randint(2, 4))]  # Random numbers

    shuffle(password_list)  # Shuffle the password list
    password = "".join(password_list)  # Convert the list to a string

    pyperclip.copy(password)  # Copy the password to the clipboard
    password_entry.insert(0, password)  # Display the password in the entry field

# Function to save the password
def save():
    website = website_entry.get()  # Get the website name
    email = email_entry.get()  # Get the email/username
    password = password_entry.get()  # Get the password

    # Check if website and password are not empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty")
    else:
        # Ask for confirmation before saving
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nEmail: {email}\nWebsite: {website}\nPassword: {password}")

        if is_ok:
            # Save the details to a text file
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels and Entry Fields
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "dummy@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()