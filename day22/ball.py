
import random
import time
from turtle import Turtle

# DIRECTIONS = [(20,20),(-20,20),(-20,-20),(20,-20)]

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.penup()
    # self.move()
    self.xMove = 8
    self.yMove = 10
    self.moveSpeed = 0.1
    
  def move(self):
    # ranD = random.randint(0,len(DIRECTIONS))
    # self.goto(ranD)
    newY = self.ycor() + self.yMove
    newX = self.xcor() + self.xMove
    self.goto(newX,newY)
    
  def bounceY(self):
    self.yMove *= -1
  
  def bounceX(self):
    self.xMove *= -1
    self.moveSpeed *= 0.95
    
  # def gameOver(self):
  #   self.goto(0,0)
  #   self.write("GAME OVER ",align="center",font=("Arial",32,"bold"))
  def resetBall(self):
    self.goto(0,0)
    time.sleep(0.6)
    self.bounceX()
    self.moveSpeed(0.1)
    