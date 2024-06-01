class User:
    def __init__(self, user_id, seats, username):
        self.id = user_id
        self.seats = seats
        self.username = username
        self.followers = 0  # Change followers to a list
        self.following = 0  # Change following to a list

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("10101", 10, "jimit")
user_2 = User("002", 9, "jack")

user_1.follow(user_2)
print(f"user 1 following: {user_1.following}")
print(f"user 2 followers: {user_2.followers}")
