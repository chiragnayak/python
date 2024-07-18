import random
import threading
from time import sleep
from turtle import Turtle


class Ball(Turtle):

    def __init__(self, screen, left_wall, right_wall, top_wall, bottom_wall):
        super().__init__()
        self.dot = None
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall

        self.speed("fastest")
        self.screen = screen
        self.setheading(random.choice([20, 40, 60, 80]))
        self.multiplier_x = random.choice([1, -1, -1, 1])
        self.multiplier_y = random.choice([1, -1, -1, 1])
        self.colours = [(251, 244, 248), (240, 249, 245), (13, 20, 78), (221, 151, 87), (32, 94, 158), (238, 228, 110),
                        (134, 24, 54), (208, 80, 117), (191, 77, 27), (50, 28, 18), (19, 45, 140), (118, 178, 218),
                        (15, 47, 27), (230, 73, 47), (3, 100, 35), (206, 131, 172), (166, 54, 85), (72, 22, 35),
                        (22, 135, 49), (141, 213, 182), (251, 225, 0), (90, 202, 160), (169, 15, 8), (94, 112, 199),
                        (85, 81, 19), (8, 175, 210), (17, 180, 141), (237, 167, 152)]
        self.forward_step = 1
        self.draw_ball(random.randint(-self.top_wall, self.top_wall), random.randint(-self.top_wall, self.top_wall))

    def draw_ball(self, x, y):
        self.penup()
        self.goto(x * self.multiplier_x, y * self.multiplier_y)
        self.speed(0)
        self.color(random.choice(self.colours))
        self.shape("circle")
        self.shapesize(1, 1, 1)

    def move(self):
        x, y = self.pos()
        if x < self.left_wall or x > self.right_wall:
            # if hit right wall or left wall
            self.multiplier_x *= -1
        elif y > self.top_wall or y < self.bottom_wall:
            # if hit bottom wall or top wall
            self.multiplier_y *= -1

        new_x = x + (self.forward_step * self.multiplier_x)
        new_y = y + (self.forward_step * self.multiplier_y)
        self.goto(new_x, new_y)
