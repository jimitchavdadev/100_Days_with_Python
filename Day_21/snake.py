from turtle import Turtle  # Import the Turtle class from the turtle module

# Define constants for the snake movement
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions for the snake segments
MOVE_DISTANCE = 20  # Distance by which the snake moves in each step

# Define constants for the directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []  # List to store the snake segments
        self.create_snake()  # Call the method to create the initial snake
        self.head = self.segments[0]  # Reference to the snake's head segment

    def create_snake(self):
        """Create the initial segments of the snake."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # Add a segment at each starting position

    def add_segment(self, position):
        """Add a new segment to the snake at the specified position."""
        new_segment = Turtle("square")  # Create a new turtle segment with square shape
        new_segment.color("white")  # Set the color of the segment to white
        new_segment.penup()  # Lift the pen to avoid drawing lines when moving
        new_segment.goto(position)  # Move the segment to the specified position
        self.segments.append(new_segment)  # Add the new segment to the snake's segments list

    def extend(self):
        """Extend the snake by adding a new segment at the end."""
        self.add_segment(self.segments[-1].position())  # Add a segment at the position of the last segment

    def move(self):
        """Move the snake by updating the positions of its segments."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the previous segment
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the previous segment
            self.segments[seg_num].goto(new_x, new_y)  # Move the current segment to the new position
        self.head.forward(MOVE_DISTANCE)  # Move the head segment forward by the move distance

    def up(self):
        """Change the snake's direction to up."""
        if self.head.heading() != DOWN:  # Avoid reversing the snake's direction
            self.head.setheading(UP)

    def down(self):
        """Change the snake's direction to down."""
        if self.head.heading() != UP:  # Avoid reversing the snake's direction
            self.head.setheading(DOWN)

    def left(self):
        """Change the snake's direction to left."""
        if self.head.heading() != RIGHT:  # Avoid reversing the snake's direction
            self.head.setheading(LEFT)

    def right(self):
        """Change the snake's direction to right."""
        if self.head.heading() != LEFT:  # Avoid reversing the snake's direction
            self.head.setheading(RIGHT)