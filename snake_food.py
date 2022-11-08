from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

    def new_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-230, 220)
        self.goto(x, y)
