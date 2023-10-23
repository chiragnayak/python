import turtle

from fun_projects.graphics.games.ping_pong.Paddle import Paddle
from fun_projects.graphics.games.ping_pong.game_frame import GameFrame
from fun_projects.graphics.games.ping_pong.message_board import MessageBoard
from fun_projects.graphics.games.ping_pong.scoreboard import Scoreboard


class PingPong:
    def __init__(self, size=3):
        self.pieces = []
        self.screen = turtle.Screen()
        self.snake_width = 20
        self.level = 0
        self.ball_speed = [(0, 200), (5, 150), (10, 100), (20, 80), (25, 70), (30, 60), (35, 50), (40, 40), (45, 35),
                           (50, 30)]
        self.size = size

        # screen
        self.screen_width = 800
        self.screen_height = 600
        self.right_wall = self.screen_width / 2
        self.left_wall = -(self.screen_width / 2)
        self.top_wall = self.screen_height / 2
        self.bottom_wall = -(self.screen_height / 2)

        self.screen.colormode(255)
        self.screen.bgcolor("black")
        self.screen.setup(self.screen_width + 100, self.screen_height + 100)
        self.screen.screensize(self.screen_width, self.screen_height)
        self.screen.title("Snake Game")

        self.screen.tracer(0)
        self.frame = GameFrame(self.screen)
        self.paddle_height = 40
        self.paddle_width = 20
        self.left_paddle = Paddle(self.screen, self.paddle_height, self.paddle_width, self.left_wall, self.top_wall, self.bottom_wall)
        self.right_paddle = Paddle(self.screen, self.paddle_height, self.paddle_width, self.right_wall, self.top_wall, self.bottom_wall)

        self.draw_table(self.left_paddle, self.right_paddle, self.top_wall, self.bottom_wall)
        self.frame = GameFrame(self.screen)
        self.scoreboard = Scoreboard(0, self.top_wall + 20)
        self.message_board = MessageBoard(self.right_wall - 80, self.top_wall + 20)


    def draw_table(self):
        self.screen


    def move_forward(self):

        # update target coordinates for each tail
        temp_head = self.head
        x, y = temp_head.pos()
        while temp_head.tail is not None:
            temp_head.tail.x, temp_head.tail.y = x, y
            temp_head = temp_head.tail
            x, y = temp_head.pos()

        # move every tail forward once head is moved
        temp_head = self.head
        temp_head.forward(20)
        temp_head.x, temp_head.y = temp_head.pos()
        while temp_head.tail is not None:
            temp_head.tail.move_forward()
            temp_head = temp_head.tail

    def move_right(self):
        current_heading = self.head.heading()
        if current_heading == 0 or current_heading == 180:
            pass
        elif current_heading == 90:
            self.head.setheading(current_heading - 90)
        elif current_heading == 270:
            self.head.setheading(current_heading + 90)

    def move_left(self):
        current_heading = self.head.heading()
        if current_heading == 0 or current_heading == 180:
            pass
        elif current_heading == 90:
            self.head.setheading(current_heading + 90)
        elif current_heading == 270:
            self.head.setheading(current_heading - 90)

    def move_up(self):
        current_heading = self.head.heading()
        if current_heading == 0 or current_heading == 270:
            self.head.setheading(current_heading + 90)
        elif current_heading == 90:
            pass
        elif current_heading == 180:
            self.head.setheading(current_heading - 90)

    def move_down(self):
        current_heading = self.head.heading()
        if current_heading == 0 or current_heading == 270:
            self.head.setheading(current_heading - 90)
        elif current_heading == 90:
            pass
        elif current_heading == 180:
            self.head.setheading(current_heading + 90)

    def check_hit_wall(self):
        x_pos, y_pos = self.head.pos()
        if x_pos >= self.right_wall or x_pos <= self.left_wall:
            print("Wall Hit Horizontal Plane")
            return True
        if y_pos >= self.top_wall or y_pos <= self.bottom_wall:
            print("Wall Hit Vertical Plane")
            return True

        return False

    def start_app(self):
        self.screen.listen()
        self.screen.onkeypress(self.move_up, "Up")
        self.screen.onkeypress(self.move_right, "Right")
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_down, "Down")
        self.screen.update()
        self.screen.exitonclick()
