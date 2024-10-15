from turtle import Turtle

bat_starting=[(-350, 0), (-350, 20), (-350, 40), (-350, 60), (-350, 80)]
bat_starting_zwei=[(350, 0), (350, 20), (350, 40), (350, 60), (350, 80)]

class Schlaeger:
    def __init__(self):
        self.create_schlaeger()
        self.creat_schlaeger_zwei()
        
        
        
    def create_schlaeger(self):
        self.bat = Turtle("square")
        self.bat.penup()
        self.bat.shapesize(5,1,1)
        self.bat.color("white")
        self.bat.goto(300, 0)
        
        
    def creat_schlaeger_zwei(self):    
        self.bat_zwei = Turtle("square")
        self.bat_zwei.penup()
        self.bat_zwei.shapesize(5,1,1)
        self.bat_zwei.color("white")
        self.bat_zwei.goto(-300, 0)
        

    def move_bat_up(self):
        if self.bat.ycor() >= 240:
            return
        self.bat.goto(x = 300, y = self.bat.ycor() + 20)
        
        
    def move_bat_down(self):
        if self.bat.ycor() <= -240:
            return
        self.bat.goto(x = 300, y = self.bat.ycor() - 20)
        
        
    def move_bat_zwei_up(self):
        if self.bat_zwei.ycor() >= 240:
            return
        self.bat_zwei.goto(x = -300, y = self.bat_zwei.ycor() + 20)
        
    def move_bat__zwei_down(self):
        if self.bat_zwei.ycor() <= -240:
            return
        self.bat_zwei.goto(x = -300, y = self.bat_zwei.ycor() - 20)