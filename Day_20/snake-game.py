from turtle import Turtle, Screen  # Import necessary classes from the turtle module
from snake import Snake  # Import the Snake class from your snake.py file
import time  # Import the time module

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off animation initially

snake = Snake()  # Create an instance of the Snake class

# Listen for key events and call the corresponding methods in the Snake class
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True  # Flag to control the game loop
while game_is_on:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Pause to control the speed of the game

    snake.move()  # Move the snake

screen.exitonclick()  # Exit the game when the screen is clicked