from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
game_is_on = True

def initiallize_scrren():
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

def start_game():
    global game_is_on
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")
    while game_is_on:
        screen.update()
        sleep(0.1)
        snake.move()

        #detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        #detect collision with wall
        if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.ycor()< -280:
            scoreboard.reset()
            snake.reset()

        #detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()
        
        
def main():
    global snake,food,scoreboard
    initiallize_scrren()
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    start_game()
    screen.exitonclick()

if __name__ == "__main__":
    main()

