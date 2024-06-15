import turtle  # Import the turtle module
import random  # Import the random module

# Setup the screen and turtle
screen = turtle.Screen()  # Create a screen object
screen.colormode(255)  # Set color mode to RGB
jimmy = turtle.Turtle()  # Create a turtle object named 'jimmy'
jimmy.speed('fastest')  # Set the turtle speed to fastest
jimmy.penup()  # Lift the pen to avoid drawing lines between dots
jimmy.hideturtle()  # Hide the turtle icon

# Function to draw a dot with a random color
def draw_dot(size):
    red = random.randint(0, 255)  # Generate a random red value
    green = random.randint(0, 255)  # Generate a random green value
    blue = random.randint(0, 255)  # Generate a random blue value
    jimmy.dot(size, (red, green, blue))  # Draw a dot with the random color

# Function to draw a grid of dots
def draw_hirst_painting(rows, cols, dot_size, spacing):
    for row in range(rows):
        for col in range(cols):
            draw_dot(dot_size)  # Call the draw_dot function to draw a dot
            jimmy.forward(spacing)  # Move the turtle forward by the spacing value
        jimmy.backward(spacing * cols)  # Move the turtle back to the start of the row
        jimmy.right(90)  # Turn the turtle 90 degrees clockwise
        jimmy.forward(spacing)  # Move the turtle up to the next row
        jimmy.left(90)  # Turn the turtle back to its original orientation

# Move the turtle to the starting position
jimmy.setheading(225)  # Set the turtle's heading to 225 degrees (bottom left corner)
jimmy.forward(300)  # Move the turtle forward by 300 units (starting position)
jimmy.setheading(0)  # Reset the turtle's heading to 0 degrees (facing right)

# Call the function to draw the Hirst painting
draw_hirst_painting(10, 10, 20, 50)  # Draw a 10x10 grid of dots with size 20 and spacing 50

# End the turtle graphics
turtle.done()  # Wait for user input to close the graphics window