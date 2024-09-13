# from turtle import Turtle, Screen
# timmy = Turtle()     #create a new object
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkBlue")   #tap into it's attributes
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon Name","Type"]
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmender","Fire"])

table.align = "l"    #for left align

print(table)