
from turtle import Turtle

class Score(Turtle):
  
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.lScore = 0
    self.rScore = 0
    self.updateScore()
   
  def updateScore(self):
    self.clear()
    self.goto(-100,200)
    self.write(self.lScore,align="center",font=('Courier',80,"bold"))
    self.goto(100,200)
    self.write(self.rScore,align="center",font=('Courier',80,"bold"))  
  def lIncrease(self):
    self.lScore += 1
    self.updateScore()
    
  def rIncrease(self):
    self.rScore += 1
    self.updateScore()