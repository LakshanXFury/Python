from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3  # Set initial lives to 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 230)
        self.write(f"Score: {self.score}  Lives: {self.lives}", align="center", font=("Courier", 30, "normal"))

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def point(self, points):  # to update the score
        self.score += points
        self.update_scoreboard()