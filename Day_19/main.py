from turtle import Turtle, Screen  # Import the Turtle and Screen classes from the turtle module
import random  # Import the random module

race = False  # Flag to control the race

# Screen Setup
screen = Screen()
screen.setup(width=700, height=800)

# Line object to draw the race track
line = Turtle()
line.hideturtle()
line.penup()
line.goto(x=230, y=150)
line.pendown()
line.setheading(270)
line.forward(300)

# Title Text
text_turtle = Turtle(visible=False)
text_turtle.penup()
text_turtle.goto(-230, 120)
text_turtle.write("Welcome to The Grand Turtle Race!", align="left", font=("Times New Roman", 16, "bold"))

# User input for bet, colors, and initial positions of turtles
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create turtles for each color and position them
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race = True  # Start the race if the user has made a bet

while race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:  # Check if any turtle has reached the finish line
            race = False  # End the race
            winner = turtle.pencolor()  # Get the color of the winning turtle
            if winner == user_bet:
                print(f"Hurray! You have won! The {winner} turtle has won the race!")
            else:
                print(f"You have lost! The {winner} turtle has won the race!")

        distance = random.randint(0, 10)  # Generate a random distance for each turtle to move
        turtle.forward(distance)  # Move the turtle forward by the random distance

screen.exitonclick()  # Exit the screen when clicked