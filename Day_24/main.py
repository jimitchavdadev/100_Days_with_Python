from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def draw_border():
    # Function to draw the game border
    border = Turtle()  # Create a Turtle object for drawing
    border.penup()  # Lift the pen to prevent drawing lines initially
    border.color("white")  # Set the border color to white
    border.hideturtle()  # Hide the turtle cursor
    border.goto(-290, 290)  # Move to the top-left corner of the screen
    border.pendown()  # Put the pen down to start drawing
    border.pensize(3)  # Set the pen size to 3 pixels
    for _ in range(4):  # Draw a rectangle with four sides
        border.forward(580)  # Draw a side of the rectangle
        border.right(90)  # Turn right to draw the next side

screen = Screen()  # Create a screen object
screen.setup(width=700, height=700)  # Set the screen dimensions
screen.bgcolor("black")  # Set the background color to black
screen.title("My Snake Game")  # Set the title of the window
screen.tracer(0)  # Turn off automatic screen updates

draw_border()  # Call the function to draw the game border

snake = Snake()  # Create a snake object
food = Food()  # Create a food object
scoreboard = Scoreboard()  # Create a scoreboard object

screen.listen()  # Start listening for keyboard inputs
screen.onkey(snake.up, "Up")  # Bind the up arrow key to the snake's up method
screen.onkey(snake.down, "Down")  # Bind the down arrow key to the snake's down method
screen.onkey(snake.left, "Left")  # Bind the left arrow key to the snake's left method
screen.onkey(snake.right, "Right")  # Bind the right arrow key to the snake's right method

game_is_on = True
while game_is_on:
    screen.update()  # Update the screen manually
    time.sleep(0.1)  # Pause for a short duration

    snake.move()  # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Refresh the food's position
        snake.extend()  # Extend the snake
        scoreboard.increase_score()  # Increase the score on the scoreboard

    # Detect collision with the wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.reset()  # Reset the scoreboard
        snake.reset()  # Reset the snake

    # Detect collision with the snake's tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()  # Reset the scoreboard
            snake.reset()  # Reset the snake

screen.exitonclick()  # Exit the game when the screen is clicked