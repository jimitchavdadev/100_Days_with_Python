from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # Initialize the superclass (Turtle)
        self.score = 0  # Initialize the score to zero
        self.color("white")  # Set the color of the scoreboard text
        self.hideturtle()  # Hide the turtle icon
        self.penup()  # Lift the pen to move without drawing
        self.goto(0, 260)  # Move the scoreboard to the top center of the screen
        self.update_scoreboard()  # Call the method to initially update the scoreboard

    def update_scoreboard(self):
        self.clear()  # Clear the previous score display
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))  # Write the updated score

    def increase_score(self):
        self.score += 1  # Increment the score by 1
        self.update_scoreboard()  # Call the method to update the scoreboard with the new score

    def game_over(self):
        self.goto(0, 0)  # Move the scoreboard to the center of the screen
        self.write("GAME OVER!", align="center", font=("Arial", 24, "normal"))  # Display the game over message