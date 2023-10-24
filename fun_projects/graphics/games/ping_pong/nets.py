from turtle import Turtle


class Nets(Turtle):

    def __init__(self, top_wall, bottom_wall):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall
        self.draw_nets()

    def draw_nets(self):
        self.goto(0, self.top_wall)
        self.right(90)
        self.pendown()
        self.forward(self.top_wall + (-self.bottom_wall))
        self.penup()
