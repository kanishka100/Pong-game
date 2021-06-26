from turtle import Turtle

FONT = ("courier", 50, "bold")
LEFT_SCORE = (100, 230)
RIGHT_SCORE = (-100, 230)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.display_score()

    def display_score(self):
        self.goto(LEFT_SCORE)
        self.write(f"{self.left_score}", align="center", font=FONT)
        self.goto(RIGHT_SCORE)
        self.write(f"{self.right_score}", align="center", font=FONT)

    def x_score(self):
        self.clear()
        self.left_score += 1
        self.display_score()

    def r_score(self):
        self.clear()
        self.right_score += 1
        self.display_score()