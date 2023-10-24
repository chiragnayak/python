import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self, screen, left_wall, right_wall, top_wall, bottom_wall, forward_step=20):
        super().__init__()
        self.dot = None
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall
        self.forward_step = forward_step

        self.speed("fastest")
        self.screen = screen
        self.setheading(random.choice([20,40, 60, 80]))
        self.draw_ball(random.randint(0, self.top_wall), random.randint(0, self.top_wall))
        self.multiplier_x = 1
        self.multiplier_y = 1

    def draw_ball(self, x, y):
        self.penup()
        self.goto(x, y)
        self.speed(0)
        self.color("yellow")
        self.shape("circle")
        self.shapesize(0.5, 0.5, 0.5)

    def move(self):
        x, y = self.pos()
        if x < self.left_wall + 10:
            # if hit left wall
            self.multiplier_x *= -1
            print("Hit left ")
        elif x > self.right_wall - 10:
            # if hit right wall
            self.multiplier_x *= -1
            print("Hit right ")
        elif y > self.top_wall - 10:
            # if hit top wall
            self.multiplier_y *= -1
            print("Hit Top ")

        elif y < self.bottom_wall + 10:
            # if hit bottom wall
            self.multiplier_y *= -1
            print("Hit Bottom ")

        new_x = x + (self.forward_step * self.multiplier_x)
        new_y = y + (self.forward_step * self.multiplier_y)

        self.goto(new_x, new_y)

