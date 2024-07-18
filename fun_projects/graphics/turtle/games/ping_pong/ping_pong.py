import time
import turtle

from fun_projects.graphics.turtle.games.ping_pong.Paddle import Paddle
from fun_projects.graphics.turtle.games.ping_pong.ball import Ball
from fun_projects.graphics.turtle.games.ping_pong.game_frame import GameFrame
from fun_projects.graphics.turtle.games.ping_pong.message_board import MessageBoard
from fun_projects.graphics.turtle.games.ping_pong.nets import Nets
from fun_projects.graphics.turtle.games.ping_pong.scoreboard import Scoreboard


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
        self.screen.colormode(255)
        self.screen.bgcolor("black")
        self.screen.setup(self.screen_width + 100, self.screen_height + 100)
        self.screen.screensize(self.screen_width, self.screen_height)
        self.screen.title("Ping Pong")

        self.frame = GameFrame(self.screen)
        self.right_wall = self.frame.screen_size[0] / 2
        self.left_wall = -(self.frame.screen_size[0] / 2)
        self.top_wall = self.frame.screen_size[1] / 2
        self.bottom_wall = -(self.frame.screen_size[1] / 2)

        self.screen.tracer(0)

        self.paddle_height = 40
        self.paddle_width = 20
        self.left_paddle = Paddle(self.screen, self.paddle_height, self.paddle_width, self.left_wall, self.top_wall, self.bottom_wall)
        self.right_paddle = Paddle(self.screen, self.paddle_height, self.paddle_width, self.right_wall, self.top_wall, self.bottom_wall)

        self.nets = Nets(self.top_wall, self.bottom_wall)
        self.ball = Ball(self.screen, self.left_wall, self.right_wall, self.top_wall, self.bottom_wall)
        self.frame = GameFrame(self.screen)
        self.left_scoreboard = Scoreboard(-40, self.top_wall)
        self.right_scoreboard = Scoreboard(+40, self.top_wall)
        self.message_board = MessageBoard(self.right_wall - 80, self.top_wall + 20)
        self.game_is_on = True

    def draw_table(self):
        pass

    def start_app(self, games=2):
        self.screen.listen()
        self.screen.onkeypress(self.left_paddle.move_up, "w")
        self.screen.onkeypress(self.left_paddle.move_down, "s")
        self.screen.onkeypress(self.right_paddle.move_up, "i")
        self.screen.onkeypress(self.right_paddle.move_down, "k")

        for plays in range(0, games):
            self.message_board.display_message(f"GAME {plays+1} of {games}")
            while True:
                time.sleep(0.0001)
                # move the ball
                self.ball.move()
                self.screen.update()

                # check top bottom wall collision : pass
                if self.ball.check_t_b_wall_collision():
                    print("TOP/BOTTOM WALL HIT ")

                # if paddle hit : left
                if self.ball.check_paddle_hit(self.left_paddle.get_range()):
                    print("LEFT PADDLE HIT ")

                if self.ball.check_paddle_hit(self.right_paddle.get_range()):
                    print("RIGHT PADDLE HIT ")

                # if hit wall left
                if self.ball.check_l_wall_collision():
                    print("LEFT WALL HIT !!!")
                    self.message_board.display_message("NEXT PLAY !!!")
                    self.right_scoreboard.increment_score()
                    self.screen.update()
                    break

                if self.ball.check_r_wall_collision():
                    print("RIGHT WALL HIT !!!")
                    self.message_board.display_message("NEXT PLAY !!!")
                    self.left_scoreboard.increment_score()
                    self.screen.update()
                    break

            time.sleep(5)
            self.ball.hideturtle() # hide previous ball
            self.ball = Ball(self.screen, self.left_wall, self.right_wall, self.top_wall, self.bottom_wall)
        self.message_board.display_message(f"GAME OVER !")
        self.screen.exitonclick()

