from turtle import Turtle  # Import the Turtle module for creating graphics

FONT = ("Courier", 24, "normal")  # Font style for the scoreboard


class Scoreboard(Turtle):
    """
    Class to manage the scoreboard in the game.
    """

    def __init__(self):
        """
        Initialize the Scoreboard object.
        """
        super().__init__()  # Initialize the Turtle object
        self.level = 1  # Initial level
        self.hideturtle()  # Hide the turtle icon
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(-280, 250)  # Move to the specified position
        self.update_scoreboard()  # Update the scoreboard initially

    def update_scoreboard(self):
        """
        Update the scoreboard with the current level.
        """
        self.clear()  # Clear the previous content
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Write the level information

    def increase_level(self):
        """
        Increase the level by 1 and update the scoreboard.
        """
        self.level += 1  # Increment the level
        self.update_scoreboard()  # Update the scoreboard with the new level

    def game_over(self):
        """
        Display the game over message in the center of the screen.
        """
        self.goto(0, 0)  # Move to the center of the screen
        self.write(f"GAME OVER", align="center", font=FONT)  # Write the game over message