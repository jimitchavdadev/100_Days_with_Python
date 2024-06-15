from turtle import Turtle

# Define constants for the snake's starting positions, movement distance, and directions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []  # List to store the snake's segments (Turtle objects)
        self.create_snake()  # Call the method to create the snake
        self.head = self.segments[0]  # Set the head of the snake as the first segment

    def create_snake(self):
        # Create the snake's initial segments at the starting positions
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Create a new segment (Turtle object) and add it to the segments list
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        # Reset the snake by moving segments out of the screen and clearing the segments list
        for seg in self.segments:
            seg.goto(1000, 1000)  # Move the segment out of the visible screen area
        self.segments.clear()  # Clear the segments list
        self.create_snake()  # Recreate the snake
        self.head = self.segments[0]  # Set the head of the snake

    def extend(self):
        # Extend the snake by adding a new segment at the end of the tail
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move the snake forward by updating the positions of its segments
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # Move the head forward by the move distance

    def up(self):
        # Change the snake's direction to up (90 degrees) if it's not already moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change the snake's direction to down (270 degrees) if it's not already moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Change the snake's direction to left (180 degrees) if it's not already moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Change the snake's direction to right (0 degrees) if it's not already moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)