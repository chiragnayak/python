from turtle import Turtle, Screen

my_turtle = Turtle()

"""
turtle object
of color red
"""
my_turtle.shape("turtle")
my_turtle.color("red")

my_turtle.begin_fill()
"""
pen - red
fill - yellow
"""
my_turtle.color("red", "yellow")
for i in range(0,4):
    my_turtle.forward(200)
    my_turtle.left(90)
    if abs(my_turtle.pos()) < 1:
        break
my_turtle.end_fill()

screen = Screen()
screen.exitonclick()