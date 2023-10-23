from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, screen, paddle_height, paddle_width, wall, top_wall, bottom_wall):
        super().__init__()
        self.paddle_height = paddle_height
        self.paddle_width = paddle_width
        self.wall = wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall

        self.speed("fastest")
        self.screen = screen
        self.penup()
        self.goto(wall, ((top_wall+bottom_wall)/2))
        self.speed(0)
        self.shape("square")
        self.shapesize(4, 1)
        self.color("white", "white")
        self.size = 20
        self.x = wall
        self.y = ((top_wall+bottom_wall)/2)