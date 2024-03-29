import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
game_is_on = True

def initiallize_scrren():
    screen.setup(width=600, height=600)
    screen.bgcolor("white")
    screen.title("Crossing Road Game")
    screen.tracer(0)

def start_game():
    global game_is_on
    screen.listen()
    screen.onkey(player.go_up, "Up")
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car.create_cars()
        car.move_cars()

        #detect collision with the car
        for cars in car.all_cars:
            if(cars.distance(player)<20):
                game_is_on = False
                scoreboard.game_over()
        
        #detect level end
        if player.is_at_finish_line():
            player.go_to_start()
            car.level_up()
            scoreboard.increase_level()
            

def main():
    global player, car, scoreboard
    initiallize_scrren()
    player = Player()
    car = CarManager()
    scoreboard = Scoreboard()
    start_game()
    screen.exitonclick()

if __name__ == "__main__":
    main()