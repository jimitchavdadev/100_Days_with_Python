from turtle import Turtle  # Import the Turtle module for creating graphics

STARTING_POSITION = (0, -280)  # Starting position of the player turtle
MOVE_DISTANCE = 10  # Distance the player turtle moves in each step
FINISH_LINE_Y = 280  # Y-coordinate of the finish line

class Player(Turtle):
    """
    Class to manage the player turtle in the game.
    """

    def __init__(self):
        """
        Initialize the Player object.
        """
        super().__init__()  # Initialize the Turtle object
        self.shape("turtle")  # Set the shape of the turtle
        self.penup()  # Lift the pen to avoid drawing lines
        self.go_to_start()  # Move the turtle to the starting position
        self.setheading(90)  # Set the initial heading of the turtle

    def go_up(self):
        """
        Move the player turtle up by the MOVE_DISTANCE.
        """
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """
        Move the player turtle to the starting position.
        """
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """
        Check if the player turtle has reached the finish line.
        """
        if self.ycor() > FINISH_LINE_Y:  # If the turtle's y-coordinate is greater than the finish line y-coordinate
            return True  # Return True, indicating that the turtle has reached the finish line
        else:
            return False  # Return False, indicating that the turtle has not reached the finish line