
from turtle import  Screen
from ball import Ball
import time
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)
screen.title('Ping Pong Game')
screen.tracer(0)

paddle1 = Paddle((-280,0))
paddle2 = Paddle((280,0))
ball = Ball()

screen.listen()
screen.onkey(paddle1.moveUp,"Up")
screen.onkey(paddle1.moveDown,"Down")
screen.onkey(paddle2.moveUp,"w")
screen.onkey(paddle2.moveDown,"s")


gameIsOn = True 

while gameIsOn:
  time.sleep(0.2)
  screen.update()
  ball.move()

screen.exitonclick() 
