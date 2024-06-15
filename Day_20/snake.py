from turtle import Turtle  # Import the Turtle class from the turtle module

# Constants for starting positions, move distance, and directions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []  # List to store the snake's segments
        self.create_snake()  # Method to create the initial snake
        self.head = self.segments[0]  # Head of the snake

    def create_snake(self):
        """Create the initial snake with three segments."""
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")  # Create a new segment as a square Turtle
            new_segment.color("white")  # Set the color of the segment
            new_segment.penup()  # Lift the pen to avoid drawing lines between segments
            new_segment.goto(position)  # Move the segment to the specified position
            self.segments.append(new_segment)  # Add the segment to the snake's segments list

    def move(self):
        """Move the snake forward by MOVE_DISTANCE."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the previous segment
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the previous segment
            self.segments[seg_num].goto(new_x, new_y)  # Move the current segment to the new position
        self.head.forward(MOVE_DISTANCE)  # Move the head of the snake forward by MOVE_DISTANCE

    def up(self):
        """Change the snake's direction to up if not currently moving down."""
        if self.head.heading() != DOWN:  # If the snake is not currently moving down
            self.head.setheading(UP)  # Change the snake's direction to up

    def down(self):
        """Change the snake's direction to down if not currently moving up."""
        if self.head.heading() != UP:  # If the snake is not currently moving up
            self.head.setheading(DOWN)  # Change the snake's direction to down

    def left(self):
        """Change the snake's direction to left if not currently moving right."""
        if self.head.heading() != RIGHT:  # If the snake is not currently moving right
            self.head.setheading(LEFT)  # Change the snake's direction to left

    def right(self):
        """Change the snake's direction to right if not currently moving left."""
        if self.head.heading() != LEFT:  # If the snake is not currently moving left
            self.head.setheading(RIGHT)  # Change the snake's direction to right