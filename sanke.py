import time
from turtle import Screen
from s_create import CreateSnake
from snake_food import Food
from snake_scoreboard import Score

snake = CreateSnake()
game_on = True

s = Screen()
s.setup(width=600, height=500,)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake.create()
food = Food()
food.new_food()


s.listen()
s.onkey(fun=snake.up, key="Up")
s.onkey(fun=snake.down, key="Down")
s.onkey(fun=snake.left, key="Left")
s.onkey(fun=snake.right, key="Right")

s.update()
score = Score()

while game_on:
    s.update()
    time.sleep(0.2)
    snake.move()

    if food.distance(snake.new[0]) < 15:
        food.new_food()
        score.clear()
        score.increase()
        snake.add()
    if snake.new[0].xcor() < - 280 or snake.new[0].xcor() > 280 \
            or snake.new[0].ycor() < -230 or snake.new[0].ycor() > 230:
        score.game_over()
        game_on = False
    # Detect collision with tail.
    # if head collide with any segment of tail then game is over
    for piece in snake.new:
        if piece == snake.new[0]:
            pass
        elif snake.new[0].distance(piece) < 15:
            score.game_over()
            game_on = False
    score.high_score()

s.exitonclick()
