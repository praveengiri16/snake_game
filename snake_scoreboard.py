from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", "r") as file:
            self.high = int(file.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", move=False, align="center", font=("Courier", 20, "bold"))

    def high_score(self):
        if self.score > self.high:
            self.high = self.score
            with open("high_score.txt", "w") as data:
                data.write(f'{self.high}')

    def update_score(self):
        self.clear()
        self.goto(0, 228)
        self.write(arg=f"Score: {self.score} High Score = {self.high}", move=False, align="center", font=("Times New Roman", 14, "normal"))

    def increase(self):
        self.score += 1
        self.update_score()

