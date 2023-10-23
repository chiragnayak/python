from turtle import Turtle


class SnakePiece(Turtle):
    def __init__(self, screen=None, x_position=0, y_position=0, head=None, tail=None):
        super().__init__()
        self.speed("fastest")
        self.screen = screen
        self.penup()
        self.goto(x_position, y_position)
        self.speed(0)
        self.shape("square")
        self.color("white", "white")
        self.size = 20
        self.x = x_position
        self.y = y_position
        self.head = head
        self.tail = tail

    def move_forward(self):
        self.goto(self.x, self.y)
