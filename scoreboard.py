from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score_p1 = 0
        self.score_p2 = 0
        self.penup()
        self.color("white")
        self.goto(-77,250)
        self.hideturtle()
        self.write(arg = f"{self.score_p1}                {self.score_p2}" , move = False, align = "left", font = ("Arial", 20, "bold"))
        
        
    def punkte_p1(self):
        self.score_p1 += 1
        self.write_neu()
    
    def punkte_p2(self):
        self.score_p2 += 1
        self.write_neu()
        
    def write_neu(self):
        self.clear()
        self.write(arg = f"{self.score_p1}                {self.score_p2}" , move = False, align = "left", font = ("Arial", 20, "bold"))
        
    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(arg = f"{self.score_p1}                {self.score_p2}" , move = False, align = "left", font = ("Arial", 20, "bold"))