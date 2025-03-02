from turtle import Turtle


class Bar(Turtle):

    def __init__(self, position):
        super().__init__()  #Gets all the properties from the Turtle
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=6)
        """ new_width = 20 * stretch_len
          = 20 * 6
          = 120 pixels """

        self.penup()
        self.goto(position)  # Move bar to the given position

    def go_left(self):
        new_x = self.xcor() - 20
        if new_x > -350:  # Prevent bar from going off the screen (left boundary)
            """min_center_x = -400 + (120 / 2)
             = -400 + 60
             = -340"""
            self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        if new_x < 350:  # Prevent bar from going off the screen (right boundary)
            """max_center_x = 400 - (120 / 2)
               = 400 - 60
               = 340
            """
            self.goto(new_x, self.ycor())
