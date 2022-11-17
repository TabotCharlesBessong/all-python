
from turtle import  Screen
from ball import Ball
import time
from paddle import Paddle
from score import Score

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)
screen.title('Ping Pong Game')
screen.tracer(0)

paddle1 = Paddle((-280,0))
paddle2 = Paddle((280,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(paddle2.moveUp,"Up")
screen.onkey(paddle2.moveDown,"Down")
screen.onkey(paddle1.moveUp,"w")
screen.onkey(paddle1.moveDown,"s")


gameIsOn = True 

while gameIsOn:
  time.sleep(0.2)
  screen.update()
  ball.move()
  
  # detecting collision with the wall and the ball 
  if ball.ycor() > 280 or ball.ycor() < -280:
    # needs to bounce the ball
    ball.bounceY()
    
  # detecting collision between ball and paddle 
  if ball.distance(paddle2) < 50 and ball.xcor() > 255 or ball.distance(paddle1) < 50 and ball.xcor() < -255 :
    ball.bounceX()
  
  if ball.xcor() > 280:
    ball.resetBall()
    score.rIncrease()
  if ball.xcor() < -280:
    ball.resetBall()
    score.lIncrease()
screen.exitonclick() 
