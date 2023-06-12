import random
import turtle


class DotPainter:
    def __init__(self, dots_horizontal=10, dots_vertical=10, density=20, size=10):
        self.dots_horizontal = dots_horizontal
        self.dots_vertical = dots_vertical
        self.density = density
        self.size = size
        self.colours = [(251, 244, 248), (240, 249, 245), (13, 20, 78), (221, 151, 87), (32, 94, 158), (238, 228, 110),
                        (134, 24, 54), (208, 80, 117), (191, 77, 27), (50, 28, 18), (19, 45, 140), (118, 178, 218),
                        (15, 47, 27), (230, 73, 47), (3, 100, 35), (206, 131, 172), (166, 54, 85), (72, 22, 35),
                        (22, 135, 49), (141, 213, 182), (251, 225, 0), (90, 202, 160), (169, 15, 8), (94, 112, 199),
                        (85, 81, 19), (8, 175, 210), (17, 180, 141), (237, 167, 152)]

        # turtle parameters
        self.my_turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.colormode(255)

        multiplier_h = dots_horizontal * (density + size)
        multiplier_v = dots_vertical * (density + size)
        horizontal = multiplier_h
        vertical = multiplier_v
        # self.screen.setup(horizontal, vertical)

        h_start = -(int(horizontal / 2)) + self.density
        v_start = -(int(vertical / 2)) + self.density

        self.starting_point = (h_start, v_start)

    def paint_dots(self, multiplier = 1.4):
        x, y = self.starting_point
        self.my_turtle.penup()
        self.my_turtle.goto(x, y)
        for row in range(0, self.dots_vertical, 1):
            y_shift = y + int (self.density * multiplier) * row
            for column in range(0, self.dots_horizontal, 1):
                x_shift = x + int (self.density * multiplier) * column
                self.my_turtle.penup()
                self.my_turtle.goto(x_shift, y_shift)
                self.my_turtle.pendown()
                self.my_turtle.dot(self.size, self.colours[random.randint(0, len(self.colours) - 1)])

        self.screen.exitonclick()


    def arrange_dots(self):
        pass


if __name__ == '__main__':
    painter = DotPainter(dots_horizontal=10, dots_vertical=10, density=40, size=20)
    painter.paint_dots()