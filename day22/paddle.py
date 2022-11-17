
from turtle import Turtle
UP = 20
DOWN = -20
XC1 = -280
XC2 = 280

class Paddle(Turtle):
  def __init__(self,position):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_wid=5,stretch_len=1)
    self.penup()
    self.goto(position)
    self.moveUp()
    
  def moveUp(self):
    newY = self.ycor() + 20
    self.goto(self.xcor(),newY)
  
  def moveDown(self):
    newY = self.ycor() - 20
    self.goto(self.xcor(),newY)