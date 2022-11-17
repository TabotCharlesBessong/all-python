
import random
from turtle import Turtle

# DIRECTIONS = [(20,20),(-20,20),(-20,-20),(20,-20)]

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.penup()
    self.move()
    
  def move(self):
    # ranD = random.randint(0,len(DIRECTIONS))
    # self.goto(ranD)
    newY = self.ycor() + 10
    newX = self.xcor() + 10
    self.goto(newX,newY)