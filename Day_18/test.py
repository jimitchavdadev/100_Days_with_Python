import turtle
import random

# Setup the screen and turtle
screen = turtle.Screen()
screen.colormode(255)  # Use RGB colors
jimmy = turtle.Turtle()
jimmy.speed('fastest')  # Speed up the turtle
jimmy.penup()  # Lift the pen so it doesn't draw lines between dots
jimmy.hideturtle()

# Function to draw a dot with a random color
def draw_dot(size):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    jimmy.dot(size, (red, green, blue))

# Function to draw a grid of dots
def draw_hirst_painting(rows, cols, dot_size, spacing):
    for row in range(rows):
        for col in range(cols):
            draw_dot(dot_size)
            jimmy.forward(spacing)
        jimmy.backward(spacing * cols)
        jimmy.right(90)
        jimmy.forward(spacing)
        jimmy.left(90)

# Move the turtle to the starting position
jimmy.setheading(225)
jimmy.forward(300)
jimmy.setheading(0)

# Call the function to draw the Hirst painting
draw_hirst_painting(10, 10, 20, 50)

# End the turtle graphics
turtle.done()
