from turtle import Turtle

class Feld:
    def __init__(self):
        pass
    
    def draw_line(self):
        line_turtle = Turtle()
        line_turtle.hideturtle()
        line_turtle.color("white")
        line_turtle.goto(0, -300)
        line_turtle.goto(0, 300)
        
    def draw_dottet_line(self):
        line_turtle = Turtle()
        line_turtle.hideturtle()
        line_turtle.color("white")
        line_turtle.penup()
        line_turtle.goto(-300, -300)
        line_turtle.pendown
        for _ in range(600):
            line_turtle.setheading(90)
            line_turtle.forward(20)
            line_turtle.penup()
            line_turtle.forward(20)
            line_turtle.pendown()
        line_turtle.penup()
        line_turtle.goto(300, -300)
        line_turtle.pendown
        for _ in range(600):
            line_turtle.setheading(90)
            line_turtle.forward(20)
            line_turtle.penup()
            line_turtle.forward(20)
            line_turtle.pendown()
        
