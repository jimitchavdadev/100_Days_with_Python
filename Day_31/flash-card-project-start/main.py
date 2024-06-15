from tkinter import *
import pandas
import random

# Define background color
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Load data from CSV file
try:
    data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# Function to show the next card
def next_card():
    global current_card, flip_timer
    # Cancel the current flip timer
    window.after_cancel(flip_timer)
    # Select a random card from the list
    current_card = random.choice(to_learn)
    # Update the card with the French word
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    # Set a timer to flip the card
    flip_timer = window.after(3000, func=flip_card)


# Function to flip the card and show the English word
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# Function to handle when a word is known
def is_known():
    to_learn.remove(current_card)
    to_learn_data = pandas.DataFrame(to_learn)
    # Save the remaining words to a new CSV file
    to_learn_data.to_csv("words_to_learn.csv", index=False)
    # Show the next card
    next_card()


# Set up the main window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# Set a timer to flip the card
flip_timer = window.after(3000, func=flip_card)

# Create a canvas for the flashcard
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 48, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

# Add buttons for marking words as known or unknown
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# Start with the first card
next_card()

# Run the Tkinter event loop
window.mainloop()
