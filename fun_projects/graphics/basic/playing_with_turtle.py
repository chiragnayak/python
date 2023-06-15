from turtle import Turtle, Screen, color, begin_fill, forward, left, pos, end_fill, done

my_turtle = Turtle()

my_turtle.shape("turtle")
my_turtle.color("red")

my_turtle.color('red', 'yellow')
my_turtle.begin_fill()
while True:
    my_turtle.forward(200)
    my_turtle.left(170)
    if abs(my_turtle.pos()) < 1:
        break
my_turtle.end_fill()

screen = Screen()
screen.exitonclick()