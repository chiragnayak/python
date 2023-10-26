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
        self.offset = 10 if self.wall > 0 else -10
        self.draw_paddle(self.wall - self.offset, 0)
        current_pos = self.pos()
        self.range = self.get_range()
        self.screen.listen()

    def draw_paddle(self, x, y):
        self.penup()
        self.goto(x, y)
        self.speed(0)
        self.shape("square")
        self.shapesize(4, 0.5, 1)
        self.color("white", "white")

    def move_up(self):
        current_pos = self.pos()
        new_x = current_pos[0]
        new_y = current_pos[1] + 10
        if (new_y + 30) >= self.top_wall:
            return
        else:
            self.goto(new_x, new_y)

        self.range = self.get_range()

    def move_down(self):
        current_pos = self.pos()
        new_x = current_pos[0]
        new_y = current_pos[1] - 10
        if (new_y - 30) <= self.bottom_wall:
            return
        else:
            self.goto(new_x, new_y)

        self.range = self.get_range()

    def get_range(self):
        current_pos = self.pos()
        offset_x = 10 if current_pos[0] < 0 else - 10
        offset_y = 40
        r = [(current_pos[0] + offset_x, current_pos[1] - offset_y),
                 (current_pos[0] + offset_x, current_pos[1] + offset_y)]
        print(r)
        return r
