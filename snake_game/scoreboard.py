from turtle import Turtle
import os
ALIGMENT = "center"
FONT = ("Arial",24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.r_w_highscore("r")
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.r_w_highscore("w")
        self.score = 0
        self.update_scoreboard()

    def r_w_highscore(self,file_mode):
        highscoreFile = os.path.dirname(__file__) +"\\highscore.txt"
        if file_mode == "w":
            with open(highscoreFile, mode= file_mode) as file:
                file.write(str(self.highscore))
        elif file_mode == "r":
            with open(highscoreFile, mode= file_mode) as file:
                self.highscore = int(file.read())

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGMENT, font=FONT)
        
        