from turtle import Turtle  # Import the Turtle module for creating graphics
import random  # Import the random module for generating random values

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]  # List of colors for cars
STARTING_MOVE_DISTANCE = 5  # Initial movement distance for cars
MOVE_INCREMENT = 10  # Amount to increase movement distance when level up


class CarManager:
    """
    Class to manage cars in the game.
    """

    def __init__(self):
        """
        Initialize the CarManager object.
        """
        self.all_cars = []  # List to store all cars
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial speed of cars

    def create_car(self):
        """
        Create a new car and add it to the list of all cars with a random chance.
        """
        random_chance = random.randint(1, 6)  # Generate a random number between 1 and 6
        if random_chance == 1:  # 1 in 6 chance to create a car
            new_car = Turtle("square")  # Create a new Turtle object representing a car
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Set the size of the car
            new_car.penup()  # Lift the pen to avoid drawing lines
            new_car.color(random.choice(COLORS))  # Set a random color for the car
            random_y = random.randint(-250, 250)  # Generate a random y-coordinate within the screen boundaries
            new_car.goto(300, random_y)  # Move the car to the right side of the screen at x=300
            self.all_cars.append(new_car)  # Add the new car to the list of all cars

    def move_cars(self):
        """
        Move all cars in the list backward (to the left) by the current car speed.
        """
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move each car backward by the car speed

    def level_up(self):
        """
        Increase the car speed when the game level up.
        """
        self.car_speed += MOVE_INCREMENT  # Increase the car speed by the move increment