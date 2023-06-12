from turtle import Turtle, Screen

my_turtle = Turtle()


my_turtle.home()
my_turtle.xcor()
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
for i in range(0,10):
    my_turtle.pendown()
    my_turtle.forward(20)
    my_turtle.penup()
    my_turtle.forward(20)
my_turtle.end_fill()

screen = Screen()
screen.exitonclick()