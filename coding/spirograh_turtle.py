import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    colours = (r, g, b)
    return colours

tim.speed("fastest")


def draw_spirograph(size_of_graph):
    for _ in range(int(360 / size_of_graph)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_graph)

draw_spirograph(5)




screen = t.Screen()
screen.exitonclick()