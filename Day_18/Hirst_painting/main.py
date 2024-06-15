import turtle as t  # Import the turtle module as 't'
import colorgram as cg  # Import the colorgram module as 'cg' for color extraction
import random  # Import the random module for generating random colors

# Define a color palette using RGB tuples
color_pallete = [
    (253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32),
    (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69),
    (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15),
    (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120),
    (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62),
    (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216),
    (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198),
    (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233),
    (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110),
    (243, 15, 14), (38, 43, 221)
]

jimmy = t.Turtle()  # Create a Turtle object named 'jimmy'
t.colormode(255)  # Set the color mode to use RGB values

jimmy.penup()  # Lift the pen to avoid drawing lines
jimmy.hideturtle()  # Hide the turtle icon
jimmy.goto(-100, -100)  # Move the turtle to the starting position
jimmy.setheading(0)  # Set the initial heading to 0 degrees (facing right)
jimmy.speed("fastest")  # Set the drawing speed to the fastest

# Define a function to create the Hirst painting
def hirst():
    for _ in range(10):  # Loop to create 10 rows
        for _ in range(10):  # Loop to create 10 dots in each row
            jimmy.dot(20, random.choice(color_pallete))  # Draw a dot with a random color from the palette
            jimmy.forward(50)  # Move the turtle forward by 50 units (spacing between dots)
        jimmy.setheading(90)  # Turn the turtle 90 degrees clockwise
        jimmy.forward(50)  # Move the turtle up by 50 units to start a new row
        jimmy.setheading(180)  # Turn the turtle 180 degrees to face left for the next row
        jimmy.forward(500)  # Move the turtle to the starting position of the next row
        jimmy.setheading(0)  # Reset the turtle's heading to 0 degrees (facing right)

hirst()  # Call the hirst function to create the Hirst painting

screen = t.Screen()  # Create a screen object to control the turtle graphics window
screen.exitonclick()  # Exit the program when the user clicks anywhere on the screen