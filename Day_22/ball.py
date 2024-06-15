from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()  # Initialize the superclass (Turtle)
        self.color("white")  # Set the color of the ball
        self.shape("circle")  # Set the shape of the ball
        self.penup()  # Lift the pen to move without drawing
        self.x_move = 10  # Set the initial x-axis movement
        self.y_move = 10  # Set the initial y-axis movement
        self.move_speed = 0.1  # Set the initial movement speed

    def move(self):
        # Calculate the new position based on current position and movement
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)  # Move the ball to the new position

    def bounce_y(self):
        # Reverse the y-axis movement to bounce off vertically
        self.y_move *= -1

    def bounce_x(self):
        # Reverse the x-axis movement and reduce speed to simulate bouncing off horizontally
        self.x_move *= -1
        self.move_speed *= 0.9  # Slow down the ball after each bounce

    def reset_position(self):
        # Reset the ball's position to the center and reset movement speed
        self.goto(0, 0)  # Move the ball to the center
        self.move_speed = 0.1  # Reset the movement speed
        self.bounce_x()  # Bounce the ball horizontally after resetting position