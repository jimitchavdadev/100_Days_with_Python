import random
import os

# ASCII art logos
logo = """
██   ██ ██  ██████  ██   ██ ███████ ██████      ██       ██████  ██     ██ ███████ ██████  
██   ██ ██ ██       ██   ██ ██      ██   ██     ██      ██    ██ ██     ██ ██      ██   ██ 
███████ ██ ██   ███ ███████ █████   ██████      ██      ██    ██ ██  █  ██ █████   ██████  
██   ██ ██ ██    ██ ██   ██ ██      ██   ██     ██      ██    ██ ██ ███ ██ ██      ██   ██ 
██   ██ ██  ██████  ██   ██ ███████ ██   ██     ███████  ██████   ███ ███  ███████ ██   ██ 
                                                                                           
"""

vs_logo = """
██    ██ ███████ 
██    ██ ██      
██    ██ ███████ 
 ██  ██       ██ 
  ████   ███████ 
"""

# Function to clear the screen
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# List of topics with their attributes
topics = [
    {'name': 'Instagram', 'follower_count': 346, 'description': 'Social media platform', 'country': 'United States'},
    # More topics here...
    {'name': 'NBA', 'follower_count': 47, 'description': 'Club Basketball Competition', 'country': 'United States'}
]

# Function to randomly choose a topic
def randomise():
    return random.choice(topics)

# Initialize score
score = 0

while True:
    # Randomly choose two topics
    title1 = random.choice(topics)
    title2 = random.choice([topic for topic in topics if topic != title1])

    # Clear screen and display game elements
    os.system("clear")
    print(logo)
    print(f"Current score: {score}")
    print(f"{title1['name']} ({title1['description']}, {title1['country']})\n {vs_logo} \n{title2['name']} ({title2['description']}, {title2['country']})")
    
    # Get player's guess
    guess = input("Type 'A' or 'B': ").lower()

    # Determine the correct answer
    max_topic = title1 if title1['follower_count'] > title2['follower_count'] else title2
    correct_answer = 'a' if max_topic == title1 else 'b'

    # Check player's guess and update score
    if guess == correct_answer:
        print("You were right!")
        score += 1
    else:
        print(f"You were wrong. {max_topic['name']} had the higher value with {max_topic['follower_count']} followers.")
        print(f"Your final score is {score}")
        break

    print(f"{max_topic['name']} had the higher value with {max_topic['follower_count']} followers.")
    print(f"Your current score is {score}")
    input("Press Enter to continue...")