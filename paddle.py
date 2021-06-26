from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pad_position):
        super().__init__()
        self.pad_position = pad_position

        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.pad_position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
