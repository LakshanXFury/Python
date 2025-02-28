from turtle import Turtle


class Bar(Turtle):

    def __init__(self, position):
        super().__init__()  #Gets all the properties from the Turtle
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.penup()
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() + 20
        self.goto(self.ycor(), new_x)

    def go_right(self):
        new_x = self.xcor() - 20
        self.goto(self.xcor(), new_x)
