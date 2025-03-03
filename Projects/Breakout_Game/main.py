from turtle import Screen, Turtle
from bar import Bar
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)  # Zero Dotted lines

bar = Bar((-100, -250))  # Move to bottom (adjust based on window size)

ball = Ball()


screen.onkey(bar.go_left, key="Left")
screen.onkey(bar.go_right, key="Right")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()  # Refresh screen continuously
    ball.move()

    # Detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:  # upper and lower
        # needs to bounce
        ball.bounce_y()
    
    if ball.xcor() > 280:
        ball.bounce_y()






screen.exitonclick()
