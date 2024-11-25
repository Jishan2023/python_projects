import time
from turtle import Screen#1st code
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen() #1st code
screen.setup(width=600, height=600) #1st code
screen.bgcolor("green") #1st code
screen.title("Welcome to my snake game.") #1st code
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_start = True #3rd code
while game_start:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detcet collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_start = False
        scoreboard.game_over()

    #detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_start = False
            scoreboard.game_over()

screen.exitonclick()