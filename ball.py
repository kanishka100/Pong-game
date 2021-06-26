from turtle import Turtle
from time import sleep

MOVE_FORWARD = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.value = 0.1
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        # print(f"new_x:{new_x}")
        # print(f"new_y:{new_y}")
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        new_x = self.xcor()
        new_y = self.ycor() + self.y_move
        # print(f" updated new_x:{new_x}")
        # print(f"updated new_y:{new_y}")
        self.goto(new_x, new_y)

    def left_bounce(self):
        self.x_move *= -1

    def right_bounce(self):
        self.x_move *= -1

    def game_reset(self):
        self.goto(0, 0)
        self.value = 0.1
        sleep(self.value)

    def speed_fast(self):
        self.value *= 0.9
        print(f"value:{round(self.value,3)}")
        sleep(self.value)
