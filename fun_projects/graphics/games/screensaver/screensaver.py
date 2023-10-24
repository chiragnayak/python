import time
import turtle

from fun_projects.graphics.games.screensaver.ball import Ball
from fun_projects.graphics.games.screensaver.game_frame import GameFrame


class ScreenSaver:
    def __init__(self, size=3):
        self.screen = turtle.Screen()
        self.size = size

        # screen
        self.screen_width = 800
        self.screen_height = 600
        self.screen.colormode(255)
        self.screen.bgcolor("black")
        self.screen.setup(self.screen_width + 100, self.screen_height + 100)
        self.screen.screensize(self.screen_width, self.screen_height)
        self.screen.title("Screensaver")

        self.frame = GameFrame(self.screen)
        self.right_wall = self.frame.screen_size[0] / 2
        self.left_wall = -(self.frame.screen_size[0] / 2)
        self.top_wall = self.frame.screen_size[1] / 2
        self.bottom_wall = -(self.frame.screen_size[1] / 2)

        self.screen.tracer(0)
        self.balls = []
        for b in range(0, 25):
            ball = Ball(self.screen, self.left_wall, self.right_wall, self.top_wall, self.bottom_wall)
            self.balls.append(ball)
        self.game_is_on = True

    def draw_table(self):
        pass

    def start_app(self):
        self.screen.listen()
        while self.game_is_on:
            self.screen.update()
            for b in range(len(self.balls)):
                self.balls[b].move()

        self.screen.exitonclick()

