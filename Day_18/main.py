import turtle as t  # Import the turtle module
import random  # Import the random module
import colorgram  # Not used in this code

# Create a turtle named 'jimmy' with specific attributes
jimmy = t.Turtle()
jimmy.shape("turtle")  # Set the turtle shape to "turtle"
jimmy.color("red")  # Set the turtle color to "red"

# Function to draw a square
def square():
    for i in range(4):
        jimmy.forward(100)
        jimmy.right(90)

# Function to draw a dashed line with alternating colors
def dashed_color():
    for _ in range(20):
        jimmy.forward(10)
        jimmy.color("white")
        jimmy.forward(10)
        jimmy.color("black")

# Function to draw a dashed line using penup and pendown
def dashed_pen():
    jimmy.color("black")
    for _ in range(20):
        jimmy.forward(10)
        jimmy.penup()
        jimmy.forward(10)
        jimmy.pendown()

# Dictionary of shapes with their sides and internal angles
shapes = {
    "triangle": [3, 180-60],
    "square": [4, 180-90],
    "pentagon": [5, 180-108],
    "hexagon": [6, 180-120],
    "heptagon": [7, 180-128.57],  # Approximately
    "octagon": [8, 180-135],
    "nonagon": [9, 180-140],
    "decagon": [10, 180-144]
}

# Function to draw a shape based on user input
def shape(aakar):
    for _ in range(shapes[aakar][0]):
        jimmy.forward(100)
        jimmy.left(shapes[aakar][1])

# Define color mode for the turtle
t.colormode(255)

# List of directions and colors for random walk
directions = [0, 90, 180, 270]
colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
    "black", "white", "gray", "cyan", "magenta", "turquoise", "gold",
    "lavender", "salmon", "coral", "aquamarine", "lime", "navy", "teal",
    "olive", "maroon", "chocolate", "indigo", "violet", "orchid", "khaki",
    "tan"
]

# Set initial pen size and speed for the turtle
jimmy.pensize(1)
jimmy.speed("fastest")

# Function to generate a random RGB color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup

# Function to perform a random walk with random colors
def random_walk():
    direction = random.choice(directions)
    jimmy.color(random_color())
    jimmy.pencolor(random_color())
    jimmy.forward(100)
    jimmy.setheading(direction)

# Function to draw a spirograph
def spirograph(gap):
    for _ in range(round(360 / gap)):
        jimmy.speed("fastest")
        jimmy.color(random_color())
        jimmy.circle(100)
        current_heading = jimmy.heading()
        jimmy.setheading(current_heading + gap)

# Set the background color of the turtle screen
t.bgcolor("LightBlue")

# Create a screen object and wait for user input to close the window
screen = t.Screen()
screen.exitonclick()