from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.update_board()

    def increase_score_left(self):
        self.left_score += 1
        self.update_board()

    def increase_score_right(self):
        self.right += 1
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score = Left {self.left_score} | Right {self.right_score}", align="center", font=('Arial', 18, 'normal'))

    def get_score(self):
        return self.right_score, self.right_score
