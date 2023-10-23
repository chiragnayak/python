import random
import turtle


class SnakeFood(turtle.Turtle):

    def __init__(self, screen=None):
        super().__init__()
        self.speed("fastest")
        self.screen = screen
        self.penup()
        self.screen_size = self.screen.screensize()
        self.x, self.y = self.get_new_coordinates()
        self.goto(self.x, self.y)
        self.speed(0)
        self.shape("circle")
        self.color("white", "yellow")
        self.shapesize(0.5,0.5,0.5)

    def if_eaten(self, head):
        x_head, y_head = round(head.xcor(), 2), round(head.ycor(), 2),
        x_food, y_food = round(self.xcor(), 2), round(self.ycor(), 2),
        print("head --", (x_head, y_head), "food ---", (x_food, y_food))
        if (x_head, y_head) == (x_food, y_food):
            self.x, self.y = self.get_new_coordinates()
            print( "food - U ---", (self.x, self.y))
            self.goto(self.x, self.y)
            return True
        else:
            return False

    def if_eaten_v2(self, head):
        if head.distance(self) < 15:
            self.x, self.y = self.get_new_coordinates()
            self.goto(self.x, self.y)
            return True
        else:
            return False

    def get_new_coordinates(self):
        range_x = [x for x in range(0,int(self.screen_size[0]/2)) if x % 20 == 0]
        range_x.extend([-x for x in range(0,int(self.screen_size[0]/2)) if x % 20 == 0])
        range_y = [y for y in range(0,int(self.screen_size[1]/2)) if y % 20 == 0]
        range_x.extend([-y for y in range(0,int(self.screen_size[1]/2)) if y % 20 == 0])
        return random.choice(range_x), random.choice(range_y),