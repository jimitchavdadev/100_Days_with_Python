from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # Initialize the superclass (Turtle)
        self.color("white")  # Set the color of the scoreboard text
        self.penup()  # Lift the pen to move without drawing
        self.hideturtle()  # Hide the turtle icon
        self.l_score = 0  # Initialize left player's score
        self.r_score = 0  # Initialize right player's score
        self.update_scoreboard()  # Update the scoreboard initially

    def update_scoreboard(self):
        self.clear()  # Clear previous scoreboard text
        self.goto(-100, 200)  # Position for left player's score
        self.write(self.l_score, align="center", font=("Courier", 88, "normal"))  # Write left player's score
        self.goto(100, 200)  # Position for right player's score
        self.write(self.r_score, align="center", font=("Courier", 88, "normal"))  # Write right player's score

    def l_point(self):
        self.l_score += 1  # Increase left player's score by 1
        self.update_scoreboard()  # Update the scoreboard with the new score

    def r_point(self):
        self.r_score += 1  # Increase right player's score by 1
        self.update_scoreboard()  # Update the scoreboard with the new score