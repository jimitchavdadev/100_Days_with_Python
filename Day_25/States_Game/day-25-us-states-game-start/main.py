import turtle  # Import the turtle module for graphics
import pandas  # Import pandas for data handling

# Create a turtle screen with a title and add a custom image
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"  # Assuming you have a custom image file
screen.addshape(image)
turtle.shape(image)

# Read state data from a CSV file into a DataFrame
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()  # Convert state names to a list
score = 0  # Initialize the player's score
guessed_states = []  # List to store guessed states

# Loop until the player guesses all 50 states or types "quit"
while score < 50:
    txt = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name?")
    if txt.lower() == "quit":
        break

    answer_state = txt.title()  # Convert the guessed state to title case
    if answer_state in all_states:  # Check if the guessed state is correct
        guessed_states.append(answer_state)  # Add the correct guess to the list
        score += 1  # Increment the score
        t = turtle.Turtle()  # Create a turtle to display the guessed state
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]  # Get data for the guessed state
        t.goto(int(state_data.x), int(state_data.y))  # Move the turtle to the state's position
        t.write(answer_state)  # Write the guessed state on the screen

# Create a list of states that the player still needs to learn
states_to_learn = [state for state in all_states if state not in guessed_states]

# Create a DataFrame from the list of states to learn and save it to a CSV file
states_to_learn_csv = pandas.DataFrame(states_to_learn)
states_to_learn_csv.to_csv("States_to_learn.csv")