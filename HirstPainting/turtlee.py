import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()
color_list = [(224, 171, 128), (146, 180, 192), (45, 104, 160), (124, 82, 93), (184, 147, 158), (129, 73, 54), (218, 230, 221), (38, 49, 66), (114, 174, 125), (177, 102, 150), (71, 6, 22), (43, 132, 104), (212, 79, 58), (236, 186, 137), (79, 96, 187), (66, 53, 43), (213, 177, 186), (113, 43, 55), (176, 184, 215), (226, 177, 164), (71, 64, 53), (174, 203, 183), (52, 57, 80), (32, 75, 91), (96, 145, 111), (80, 58, 50), (165, 200, 205)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()