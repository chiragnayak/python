import random
import turtle
from turtle import Turtle, Screen
from random import randint


class Racer:

    def __init__(self, screen, color=None, position_tuple = None):
        self.my_turtle = turtle.Turtle()
        self.my_turtle.shape("turtle")
        self.screen = screen
        if color is None:
            self.my_turtle.color(self.get_rand_color(),self.get_rand_color())
        else:
            self.color = color
            self.my_turtle.color(color, color )

        self.my_turtle.penup()
        self.my_turtle.goto(x=position_tuple[0], y=position_tuple[1])

    def move_to_finish(self, limit):
        while True:
            self.my_turtle.forward(self.random_steps())
            x, y = self.my_turtle.pos()
            if x >= limit:
                break
        print(self.color, "reached !")

    def move(self):
        self.my_turtle.forward(self.random_steps())

    def random_steps(self):
        return random.randint(0, 10)

    def get_rand_color(self):
        return randint(0, 255), randint(0, 255), randint(0, 255)


class Race:

    def __init__(self):
        self.count = 6
        self.colors = ["red", "green", "blue", "orange", "pink", "brown"]
        self.screen = Screen()
        bet = self.screen.textinput("Place your bet on color.", "red, green, blue, orange, pink, brown" )
        self.screen.colormode(255)
        x = 500
        y = 500
        self.screen.setup(x, y)
        self.racers = []

        gap = 20
        start_position_y = y/2 - int(y / self.count) + gap
        start_position_x = -(x/2 - gap)

        self.threads = []
        for r in range(0, self.count):
            self.racers.append(Racer(self.screen, color=self.colors[r], position_tuple=(start_position_x, start_position_y)))
            start_position_y -= 50

        """
        NOT WORKING: next turtle moves when first one completes
        ref : https://stackoverflow.com/questions/19498447/multithreading-with-python-turtle
        for r in range(0, len(self.racers)):
            thread = threading.Thread(target=self.racers[r].move_to_finish(x/2))
            thread.daemon = True
            self.threads.append(thread)

        for t in range(0, len(self.threads)):
            self.threads[t].start()

        for t in range(0, len(self.threads)):
            self.threads[t].join()"""

        race_is_on = True
        while race_is_on:
            for r in range(0, self.count):
                turtle = self.racers[r]
                if turtle.my_turtle.xcor() > (x/2-10):
                    win_color = turtle.my_turtle.pencolor()
                    print(turtle.my_turtle.pencolor(), "Won !!")
                    if win_color == bet :
                        print ("You Won the bet !")
                    else:
                        print("Sad !! You Lost the bet !")
                    race_is_on = False
                    break
                turtle.move()

        self.screen.exitonclick()


if __name__ == '__main__':
    r = Race()
