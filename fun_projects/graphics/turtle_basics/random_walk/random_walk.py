import random
import turtle
from random import randint
from turtle import Turtle, Screen


class RandomWalk():

    def __init__(self, screen_size=500, step_size=20, steps_to_take=500, use_heading = False ):
        self.xLoc = 0
        self.yLoc = 0
        self.my_turtle = turtle.Turtle()
        self.color = "red"
        self.screen = Screen()
        self.width = self.my_turtle.width(7)
        # set screen size
        self.screen_size = screen_size
        self.screen.setup(self.screen_size, self.screen_size)
        self.limit = self.screen_size / 2
        self.step_size = step_size
        self.steps_to_take = steps_to_take
        self.use_heading = use_heading

        # set color mode
        self.screen.colormode(255)

    def get_rand_color(self):
        self.my_turtle.pencolor(randint(0, 255),
                                randint(0, 255),
                                randint(0, 255))

    def take_random_direction_and_step(self, stepSize):
        self.get_rand_color()
        if self.use_heading:
            self.my_turtle.setheading(random.choice([0, 90, 180, 270]))
            self.my_turtle.forward(stepSize)
        else:
            dir = random.randint(0, 3)
            if self.check_if_hitting_wall(dir):
                return
            if dir == 0:
                self.my_turtle.right(90)
                self.my_turtle.forward(stepSize)
            elif dir == 1:
                self.my_turtle.left(90)
                self.my_turtle.forward(stepSize)
            elif dir == 2:
                self.my_turtle.backward(stepSize)
            else:
                self.my_turtle.forward(stepSize)

    def take_steps(self, xLoc=0, yLoc=0):
        step = 0
        self.my_turtle.setposition(xLoc, yLoc)
        while step < self.steps_to_take:
            self.take_random_direction_and_step(self.step_size)
            step += 1

        screen = Screen()
        screen.exitonclick()

    def check_if_hitting_wall(self, dir):
        """
        right limit = x = 250
        top limit  = y = 250
        bottom limit = y = -250
        left limit = x = -250
        """
        (xPos, yPos) = self.my_turtle.position()
        if xPos >= self.limit or xPos <= -self.limit or yPos >= self.limit or yPos <= -self.limit:
            # go backwards
            self.my_turtle.right(180)
            self.my_turtle.forward(self.step_size * 3)
            return True
        else:
            return False


if __name__ == '__main__':
    rWalk = RandomWalk(screen_size=500, step_size=20, steps_to_take=200, use_heading=False)
    rWalk.take_steps()
