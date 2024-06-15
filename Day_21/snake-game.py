from turtle import Screen  # Import the Screen class from the turtle module
from snake import Snake  # Import the Snake class from your snake module
from food import Food  # Import the Food class from your food module
from scoreboard import Scoreboard  # Import the Scoreboard class from your scoreboard module
import time  # Import the time module for time-related operations

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off screen updates to manually control when the screen updates

# Create instances of Snake, Food, and Scoreboard classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for keyboard input
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True  # Flag to control the game loop
while game_is_on:
    screen.update()  # Update the screen to show changes
    time.sleep(0.1)  # Pause for a short time to control the game speed
    snake.move()  # Move the snake in each iteration of the game loop

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Move the food to a new random position
        scoreboard.increase_score()  # Increase the score
        snake.extend()  # Extend the snake's length

    # Detect collision with the wall
    if (
        snake.head.xcor() > 260
        or snake.head.xcor() < -260
        or snake.head.ycor() > 260
        or snake.head.ycor() < -260
    ):
        game_is_on = False  # End the game loop
        scoreboard.game_over()  # Display game over message

    # Detect collision with the snake's tail
    for segment in snake.segments:
        if segment == snake.head:
            pass  # Skip checking collision with the head itself

        elif snake.head.distance(segment) < 10:
            game_is_on = False  # End the game loop
            scoreboard.game_over()  # Display game over message

screen.exitonclick()  # Close the game window when clicked