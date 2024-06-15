class User:
    def __init__(self, user_id, seats, username):
        self.id = user_id
        self.seats = seats
        self.username = username
        self.followers = []  # Change followers to a list
        self.following = []  # Change following to a list

    def follow(self, user):
        user.followers.append(self)  # Add the follower to the other user's followers list
        self.following.append(user)  # Add the user to the current user's following list

user_1 = User("10101", 10, "jimit")
user_2 = User("002", 9, "jack")

user_1.follow(user_2)
print(f"user 1 following: {len(user_1.following)}")  # Output: user 1 following: 1
print(f"user 2 followers: {len(user_2.followers)}")  # Output: user 2 followers: 1