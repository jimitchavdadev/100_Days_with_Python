from turtle import Turtle, Screen
import random

race = False    # race start fla
screen = Screen()   # Screen Setup
screen.setup(width=700, height=800)

# Line object to draw the line
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

# User bet, colors, position
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race = True

while race:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"Hurray! You have won! The {winner} turtle has won the race!")
            else:
                print(f"You have lost! The {winner} turtle has won the race!")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
