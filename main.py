from turtle import Screen
from schlaeger import Schlaeger
from feld import Feld
import time
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
schlaeger = Schlaeger()
feld = Feld()
ball = Ball()
scoreboard = ScoreBoard()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
game_is_on = False


feld.draw_line()
feld.draw_dottet_line()


screen.onkeypress(fun = schlaeger.move_bat_up, key = "w")
screen.onkeypress(fun = schlaeger.move_bat_down, key = "s")
screen.onkeypress(fun = schlaeger.move_bat_zwei_up, key = "Up")
screen.onkeypress(fun = schlaeger.move_bat__zwei_down, key = "Down")


game_is_on = True
while game_is_on:
    richtung = ball.heading()
    
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.setheading(-richtung)
        
    if schlaeger.bat.distance(ball) < 40:
        ball.setheading(180 -richtung)
    elif schlaeger.bat_zwei.distance(ball) < 40:
        ball.setheading(180 - richtung)
    
    if ball.xcor() >= 350:
        scoreboard.punkte_p2()
        ball.teleport(0,0)
        time.sleep(0.5)
        ball.move()
    elif ball.xcor() <= -350:
        scoreboard.punkte_p1()
        ball.teleport(0,0)
        time.sleep(0.5)
        ball.move()
        
    screen.update()
    ball.move()
    time.sleep(0.005)
screen.exitonclick()