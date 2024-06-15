from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()  # Initialize the superclass (Turtle)
        self.shape("square")  # Set the shape of the paddle
        self.color("white")  # Set the color of the paddle
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the paddle's size
        self.penup()  # Lift the pen to move without drawing
        self.goto(position)  # Set the initial position of the paddle

    def go_up(self):
        new_y = self.ycor() + 20  # Calculate the new y-coordinate for moving up
        self.goto(self.xcor(), new_y)  # Move the paddle to the new position

    def go_down(self):
        new_y = self.ycor() - 20  # Calculate the new y-coordinate for moving down
        self.goto(self.xcor(), new_y)  # Move the paddle to the new position