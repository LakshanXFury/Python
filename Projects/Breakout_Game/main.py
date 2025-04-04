from turtle import Screen, Turtle
from bar import Bar
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)  # Zero Dotted lines

bar = Bar((-100, -250))  # Move to bottom (adjust based on window size)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(bar.go_left, key="Left")
screen.onkey(bar.go_right, key="Right")

# Create bricks in a row
bricks = []
x_start = -330  # Starting x position
y_start = 200  # Y position of bricks
brick_spacing = 70  # Space between bricks

rows = 3
colors = ["red", "orange", "yellow"]

# Red should be 5, orange 3 and yellow 1

for row in range(rows):
    for i in range(10):
        new_brick = Brick((x_start + i * brick_spacing, y_start - (row * 30)))
        new_brick.color(colors[row])
        bricks.append(new_brick)  # Store bricks in a list

# Main game loop
game_is_on = True
while game_is_on:

    time.sleep(ball.movespeed)
    screen.update()  # Refresh screen continuously
    ball.move()

    # Detect the collision with wall
    if ball.ycor() > 290:  # upper
        # needs to bounce
        ball.bounce_y()

    # Detect ball missing the bar (lose a life)
    if ball.ycor() < -290:  # If ball falls below the screen
        scoreboard.lose_life()  # Reduce a life
        time.sleep(1)  # Pause before deciding the next action
        if scoreboard.lives == 0:
            game_is_on = False  # End game when lives reach 0
            scoreboard.goto(0, 0)
            scoreboard.write("GAME OVER", align="center", font=("Courier", 30, "normal"))
        else:
            ball.reset_position()  # Reset the ball position if lives remain

    if ball.xcor() > 380 or ball.xcor() < -380:  # Adjust for ball size , bounce logic for left and right
        ball.bounce_x()  # Ball should bounce in the X direction

    # Detect collision with the bar
    if ball.distance(bar) < 50 and ball.ycor() < -230:
        ball.bounce_y()

    # Detect collision with bricks
    for brick in bricks:
        if ball.distance(brick) < 40:  # If ball hits a brick
            brick_color = brick.fillcolor()  # Get the color of the brick
            if brick_color == "red":
                points = 5
            elif brick_color == "orange":
                points = 3
            elif brick_color == "yellow":
                points = 1

            scoreboard.point(points)  # From scoreboard

            scoreboard.update_scoreboard()  # Update the score display
            brick.hideturtle()  # Hide the brick
            bricks.remove(brick)  # Remove from list
            ball.bounce_y()
            break  # Stop checking once a brick is hit

screen.exitonclick()
