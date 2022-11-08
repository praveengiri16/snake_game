from turtle import Turtle


class CreateSnake:
    def __init__(self):
        self.new = []

    def create(self):
        x = 0
        for i in range(3):
            tim = Turtle("square")
            tim.penup()
            tim.color("white")
            tim.goto(x, 0)
            x -= 20
            self.new.append(tim)

    def add(self):
        tim = Turtle('square')
        x_position = self.new[-1].xcor()
        y_position = self.new[-1].ycor()
        tim.color("white")
        tim.penup()
        tim.goto(x_position, y_position)
        self.new.append(tim)

    def move(self):
        for num in range(len(self.new) - 1, 0, -1):
            updated_x = self.new[num - 1].xcor()
            updated_y = self.new[num - 1].ycor()
            self.new[num].goto(x=updated_x, y=updated_y)
        self.new[0].forward(20)

    def up(self):
        if self.new[0].heading() != 270:
            self.new[0].setheading(90)

    def left(self):
        if self.new[0].heading() != 0:
            self.new[0].setheading(180)

    def right(self):
        if self.new[0].heading() != 180:
            self.new[0].setheading(0)

    def down(self):
        if self.new[0].heading() != 90:
            self.new[0].setheading(270)
