from turtle import Turtle

ALIGNMENT = "center"  # Text alignment for the scoreboard
FONT = ("Courier", 24, "normal")  # Font style for the scoreboard

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # Initialize the Turtle object
        self.score = 0  # Current score
        # Try to read the high score from a file, set to 0 if file doesn't exist or is invalid
        try:
            with open("data.txt") as data:
                self.high_score = int(data.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0
        self.color("white")  # Set text color to white
        self.penup()  # Lift the pen to prevent drawing lines
        self.goto(0, 285)  # Position the scoreboard at the top center
        self.hideturtle()  # Hide the turtle cursor
        self.update_scoreboard()  # Update the scoreboard with current scores

    def update_scoreboard(self):
        # Clear previous score and write new score and high score on the screen
        self.clear()  # Clear previous text
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        # Reset the score and update the scoreboard, update high score if necessary
        if self.score > self.high_score:
            self.high_score = self.score  # Update high score if current score is higher
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")  # Write high score to file
        self.score = 0  # Reset current score to 0
        self.update_scoreboard()  # Update scoreboard with new scores

    def increase_score(self):
        # Increase the score by 1 and update the scoreboard
        self.score += 1  # Increase current score
        self.update_scoreboard()  # Update scoreboard with new scores