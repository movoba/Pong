from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape = "circle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color("white")
        self.seth(20)
        
    def move(self):
        self.forward(2)
        