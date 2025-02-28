from turtle import Screen, Turtle
from bar import Bar

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)  # Zero Dotted lines

bar = Bar((-100, -250))  # Move to bottom (adjust based on window size)








screen.exitonclick()
