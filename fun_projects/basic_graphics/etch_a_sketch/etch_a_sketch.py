import turtle
from random import randint


class EtchASketch:

    def __init__(self):
        self.my_turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.colormode(255)

    def start_app(self):
        self.screen.listen()
        self.screen.onkeypress(self.move_forwards, "w")
        self.screen.onkeypress(self.move_backwards, "s")
        self.screen.onkeypress(self.turn_right, "d")
        self.screen.onkeypress(self.turn_left, "a")
        self.screen.onkeypress(self.hop, "space")
        self.screen.onkeypress(self.clear, "BackSpace")
        self.screen.onkeypress(self.color_change, "c")
        self.screen.exitonclick()

    def get_rand_color(self):
        self.my_turtle.pencolor(randint(0, 255),
                                randint(0, 255),
                                randint(0, 255))

    def move_forwards(self):
        self.my_turtle.forward(10)

    def move_backwards(self):
        self.my_turtle.backward(10)

    def turn_right(self):
        self.my_turtle.right(10)

    def turn_left(self):
        self.my_turtle.left(10)

    def hop(self):
        self.my_turtle.penup()
        self.move_forwards()
        self.my_turtle.pendown()

    def color_change(self):
        self.get_rand_color()

    def clear(self):
        self.my_turtle.penup()
        self.my_turtle.clear()
        self.my_turtle.home()
        self.my_turtle.pendown()


if __name__ == '__main__':
    eas = EtchASketch()
    eas.start_app()