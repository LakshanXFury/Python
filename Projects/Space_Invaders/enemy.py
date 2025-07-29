from turtle import Turtle
import random


class Enemy(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(position)
        self.direction = 1

    def move(self):
        x = self.xcor() + 5 * self.direction
        if x > 380 or x < -380:
            self.direction *= -1  # Reverse direction
            y = self.ycor() - 20  # Move down a row
            self.sety(y)
        self.setx(x)