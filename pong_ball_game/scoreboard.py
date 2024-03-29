from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial",24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align=ALIGMENT, font=FONT)

    def increase_score_r(self):
        self.r_score += 1
        self.update_scoreboard()

    def increase_score_l(self):
        self.l_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGMENT, font=FONT)
        
        