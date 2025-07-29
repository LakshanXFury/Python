from turtle import Turtle


class SpaceShip(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("green")
        self.shape("triangle")
        self.penup()
        self.goto(position)
        self.setheading(90)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
