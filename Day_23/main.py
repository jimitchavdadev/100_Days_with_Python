import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns off animation

# Create player, car manager, and scoreboard objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for player input
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Pause for a short duration
    screen.update()  # Update the screen to show changes

    # Create and move cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # Check distance between player and cars
            game_is_on = False  # End the game
            scoreboard.game_over()  # Display game over message

    # Detect successful crossing of the finish line
    if player.is_at_finish_line():
        player.go_to_start()  # Reset player position
        car_manager.level_up()  # Increase car speed
        scoreboard.increase_level()  # Increase game level

# Keep the window open until clicked
screen.exitonclick()