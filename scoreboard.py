from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.clear()
        self.penup()
        self.color("white")
        self.goto(0, 270)


        self.write(f"Score : {self.score} ", align="center", font=("Arial", 20, "bold"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score} ", align="center", font=("Arial", 20, "bold"))

    def end_game(self):
        self.goto(0,0)
        self.write("Game over", align= "center", font=("Arial", 20, "bold"))