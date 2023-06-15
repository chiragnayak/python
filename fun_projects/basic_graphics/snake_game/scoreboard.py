from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.update_board()

    def increase_score(self):
        self.score += 1
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=('Arial', 18, 'normal'))

    def get_score(self):
        return self.score
