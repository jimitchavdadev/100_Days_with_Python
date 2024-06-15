from turtle import Turtle  # Import the Turtle class from the turtle module
import random  # Import the random module for generating random coordinates

class Food(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the parent class (Turtle)
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Lift the pen to avoid drawing lines when moving
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Stretch the circle shape
        self.color("yellow")  # Set the color of the food to yellow
        self.speed("fastest")  # Set the animation speed to fastest
        self.refresh()  # Call the refresh method to initialize the food's position

    def refresh(self):
        """Move the food to a random position within the screen."""
        random_x = random.randint(-250, 250)  # Generate a random x-coordinate within the screen boundaries
        random_y = random.randint(-250, 250)  # Generate a random y-coordinate within the screen boundaries
        self.goto(random_x, random_y)  # Move the food to the random position