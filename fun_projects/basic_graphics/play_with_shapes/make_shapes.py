import turtle
from random import randint
from turtle import Turtle, Screen


class DrawShapes() :

    def __init__(self, turtleShape = "Arrow", turtleColor = "red"):
        self.xLoc = 0
        self.yLoc = 0
        self.my_turtle = turtle.Turtle()
        self.color = "red"
        self.screen = Screen()
        self.width = self.my_turtle.width(3)

        # set color mode
        self.screen.colormode(255)

    def draw_shapes(self):
        self.draw_shape(self.xLoc, self.yLoc, 3)
        self.draw_shape(self.xLoc, self.yLoc, 4)
        self.draw_shape(self.xLoc, self.yLoc, 5)
        self.draw_shape(self.xLoc, self.yLoc, 6)
        self.draw_shape(self.xLoc, self.yLoc, 7)
        self.draw_shape(self.xLoc, self.yLoc, 8)
        self.draw_shape(self.xLoc, self.yLoc, 9)

        screen = Screen()
        screen.exitonclick()

    def get_rand_color(self):
        self.my_turtle.pencolor(randint(0, 255),
                            randint(0, 255),
                            randint(0, 255))

    def draw_shape(self, xLoc, yLoc, sides, sideLen = 100):
        if sides == 0:
            return
        angle = 360 / sides
        self.get_rand_color()
        """
        - start, forward x side
        while:
            - turn by angle
            - draw side
            if reach xLoc, yLoc
             break
        """
        while True:
            print("-->",self.my_turtle.pos(), abs(self.my_turtle.pos()))
            self.my_turtle.forward(sideLen)
            self.my_turtle.right(angle)
            # if reach to start position
            if abs(self.my_turtle.pos()) < 1:
                 break


if __name__ == '__main__':
    printer = DrawShapes()
    printer.draw_shapes()