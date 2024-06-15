from turtle import Turtle  # Import Turtle class from the turtle module
import random  # Import the random module for generating random numbers

class Food(Turtle):  # Create a Food class that inherits from Turtle

    def __init__(self):  # Constructor method for initializing the Food object
        super().__init__()  # Call the constructor of the Turtle class
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Lift the pen to prevent drawing lines
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Resize the circle
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the animation speed to the fastest
        self.refresh()  # Call the refresh method to reposition the food

    def refresh(self):  # Method to reposition the food
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate
        self.goto(random_x, random_y)  # Move the food to the random position