from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.shapesize(stretch_wid=0.2, stretch_len=1)
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.speed(0)

    def move(self):
        self.forward(20)