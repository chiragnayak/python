
import turtle


class GameFrame(turtle.Turtle):

    def __init__(self, screen=None):
        super().__init__()
        self.speed("fastest")
        self.pencolor("red")
        self.hideturtle()
        self.screen = screen
        self.screen_size = self.screen.screensize()
        self.x, self.y = round(int(self.screen_size[0]/2), 0), round(int(self.screen_size[1]/2), 0)
        self.penup()
        self.goto(self.x, self.y)
        self.speed(0)
        self.pendown()
        self.right(90)
        self.forward(self.screen_size[1])
        self.right(90)
        self.forward(self.screen_size[0])
        self.right(90)
        self.forward(self.screen_size[1])
        self.right(90)
        self.forward(self.screen_size[0])