from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep


screen = Screen()
game_is_on = True

def initiallize_scrren():
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.tracer(0)

def start_game():
    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")
    while game_is_on:
        sleep(ball.move_speed)
        screen.update()
        ball.move()

        #detect collision with the wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        #detect collision with the paddle
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        #detect R paddle lose
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.increase_score_l()

        #detect L paddle lose
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.increase_score_r()
    
def main():
    global r_paddle, l_paddle, ball, scoreboard
    initiallize_scrren()
    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()
    start_game()
    screen.exitonclick()

if __name__ == "__main__":
    main()

