import turtle
from time import sleep

from fun_projects.graphics.turtle.games.snake.game_frame import GameFrame
from fun_projects.graphics.turtle.games.snake.message_board import MessageBoard
from fun_projects.graphics.turtle.games.snake.scoreboard import Scoreboard
from fun_projects.graphics.turtle.games.snake.snake_food import SnakeFood
from fun_projects.graphics.turtle.games.snake.snake_piece import SnakePiece


class Snake:
    def __init__(self, size=3):
        self.pieces = []
        self.screen = turtle.Screen()
        self.snake_width = 20
        self.level = 0
        self.food_speed = [(0, 200), (5, 150), (10, 100), (20, 80), (25, 70), (30, 60), (35, 50), (40, 40), (45, 35),
                           (50, 30)]
        self.size = size

        # screen
        self.screen_width = 600
        self.screen_height = 600
        self.right_wall = self.screen_width / 2
        self.left_wall = -(self.screen_width / 2)
        self.top_wall = self.screen_height / 2
        self.bottom_wall = -(self.screen_width / 2)

        self.screen.colormode(255)
        self.screen.bgcolor("black")
        self.screen.setup(self.screen_width + 100, self.screen_height + 100)
        self.screen.screensize(self.screen_width, self.screen_height)
        self.screen.title("Snake Game")

        self.screen.tracer(0)
        self.frame = GameFrame(self.screen)
        self.head = SnakePiece(screen=self.screen, x_position=0, y_position=0, head=None, tail=None)
        self.tail = SnakePiece(screen=self.screen, x_position=-20, y_position=0, head=None, tail=None)
        self.head.tail = self.tail
        self.tail.head = self.head
        self.food = SnakeFood(self.screen)
        self.scoreboard = Scoreboard(0, self.top_wall + 20)
        self.message_board = MessageBoard(self.right_wall - 80, self.top_wall + 20)

    def check_hit_self(self):
        temp_head = self.head
        x_head, y_head = round(self.head.xcor(), 2), round(self.head.ycor(), 2)
        temp_head = temp_head.tail
        while temp_head.tail is not None:
            x_tail, y_tail = round(temp_head.tail.xcor(), 2), round(temp_head.tail.ycor(), 2),
            if (x_head, y_head) == (x_tail, y_tail):
                print("Self Hit !")
                return True
            else:
                temp_head = temp_head.tail

        return False

    def run_snake(self):
        while True:
            self.screen.update()  # update when all process is done and everything is at required position
            if not (self.check_hit_wall() or self.check_hit_self()):
                self.move_forward()
                x_food, y_food = self.food.pos()
                if self.food.if_eaten_v2(self.head):
                    self.scoreboard.increase_score()
                    score = self.scoreboard.get_score()
                    if score == self.food_speed[self.level + 1][0]:
                        self.level += 1
                        self.message_board.display_message("Level : {}".format(self.level))
                    new_head = SnakePiece(screen=self.screen, x_position=x_food, y_position=y_food, head=None,
                                          tail=self.head)
                    new_head.setheading(self.head.heading())
                    self.head = new_head
                if self.level <= len(self.food_speed):
                    sleep(self.food_speed[self.level][1] / 1000)
            else:
                self.message_board.display_message("GAVE OVER !!")
                break

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
        self.run_snake()
        self.screen.exitonclick()
