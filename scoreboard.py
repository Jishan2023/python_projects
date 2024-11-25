from turtle import Turtle
alignment = 'center'
fonts = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=alignment, font=fonts)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=alignment, font=fonts)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()