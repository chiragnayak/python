from turtle import Turtle


class MessageBoard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.display_message("PLAY")

    def display_message(self, message):
        self.clear()
        self.write(f"{message}", align="center", font=('Arial', 18, 'normal'))

