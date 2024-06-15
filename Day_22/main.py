from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Turn off animation

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))  # Create the right paddle
l_paddle = Paddle((-350, 0))  # Create the left paddle
ball = Ball()  # Create the ball
scoreboard = Scoreboard()  # Create the scoreboard

# Listen for key presses to control paddles
screen.listen()
screen.onkey(r_paddle.go_up, "Up")  # Move the right paddle up
screen.onkey(r_paddle.go_down, "Down")  # Move the right paddle down
screen.onkey(l_paddle.go_up, "w")  # Move the left paddle up
screen.onkey(l_paddle.go_down, "s")  # Move the left paddle down

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Control ball movement speed
    screen.update()  # Update the screen
    ball.move()  # Move the ball

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # Bounce off the top and bottom walls

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()  # Bounce off the paddles

    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()  # Reset ball position
        scoreboard.l_point()  # Increase left paddle's score

    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()  # Reset ball position
        scoreboard.r_point()  # Increase right paddle's score

# Exit the game when clicking on the screen
screen.exitonclick()