class User:
    def __init__(self, user_id, username):    #Constructor
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):   #Method
        user.follower += 1
        self.following += 1



user_1 = User("017","Lakshan")
user_2 = User("007","Bond")
# print(user_2.username)
# print(user_1.follower)

user_1.follow(user_2)    #follow method
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)

# print(f"My name is {user_1.name} and my roll no is {user_1.id}")
