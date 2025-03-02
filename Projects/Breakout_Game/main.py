from turtle import Screen, Turtle
from bar import Bar

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)  # Zero Dotted lines

bar = Bar((-100, -250))  # Move to bottom (adjust based on window size)


screen.listen()
screen.onkey(bar.go_left, key="Left")
screen.onkey(bar.go_right, key="Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Refresh screen continuously





screen.exitonclick()
