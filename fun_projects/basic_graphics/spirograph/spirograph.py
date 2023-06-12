import turtle
from random import randint


class Spirograph:

    def __init__(self, radius=100, diff = 2):
        self.my_turtle = turtle.Turtle()
        self.my_turtle.speed("fastest")
        self.radius = radius
        self.screen = turtle.Screen()
        self.diff = diff
        self.screen.colormode(255)

    def get_rand_color(self):
        self.my_turtle.pencolor(randint(0, 255),
                                randint(0, 255),
                                randint(0, 255))

    def draw(self):
        for _ in range(int(360/self.diff)):
                self.get_rand_color()
                self.my_turtle.circle(self.radius)
                self.my_turtle.setheading(self.my_turtle.heading() + self.diff)

        self.screen.exitonclick()


if __name__ == '__main__':
    rWalk = Spirograph(radius=100, diff = 10)
    rWalk.draw()
