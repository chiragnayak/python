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
        self.draw_paddle(self.wall, 0)
        self.screen.listen()

    def draw_paddle(self, x, y):
        self.penup()
        self.goto(x, y)
        self.speed(0)
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white", "white")

    def move_up(self):
        current_pos = self.pos()
        new_x = current_pos[0]
        new_y = current_pos[1]+20
        if (new_y + 60) > self.top_wall:
            return
        else:
            self.draw_paddle(new_x, new_y)

    def move_down(self):
        current_pos = self.pos()
        new_x = current_pos[0]
        new_y = current_pos[1] - 20
        if (new_y - 40) <= self.bottom_wall:
            return
        else:
            self.draw_paddle(new_x, new_y)