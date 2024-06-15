from turtle import Turtle, Screen  # Import the Turtle and Screen classes from the turtle module

# Create a turtle named 'tim' and a screen object
tim = Turtle()
screen = Screen()

# Function to clear the screen and reset the turtle's position
def clear():
    tim.clear()  # Clear the turtle's drawings
    tim.penup()  # Lift the pen
    tim.home()  # Move to the home position (origin)
    tim.pendown()  # Lower the pen to start drawing again

# Function to move the turtle forward
def move_forward():
    tim.forward(10)  # Move the turtle forward by 10 units

# Function to move the turtle backward
def move_backwards():
    tim.backward(10)  # Move the turtle backward by 10 units

# Function to turn the turtle left
def turn_left():
    new_heading = tim.heading() + 10  # Increase the current heading by 10 degrees
    tim.setheading(new_heading)  # Set the new heading for the turtle

# Function to turn the turtle right
def turn_right():
    new_heading = tim.heading() - 10  # Decrease the current heading by 10 degrees
    tim.setheading(new_heading)  # Set the new heading for the turtle

# Listen for key events and associate them with corresponding functions
screen.listen()  # Start listening for events
screen.onkey(move_forward, "w")  # Press 'w' to move forward
screen.onkey(move_backwards, "s")  # Press 's' to move backward
screen.onkey(turn_left, "a")  # Press 'a' to turn left
screen.onkey(turn_right, "d")  # Press 'd' to turn right
screen.onkey(clear, "c")  # Press 'c' to clear the screen and reset

# Exit the screen when clicked
screen.exitonclick()