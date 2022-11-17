
from turtle import Turtle
class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.highScore = 0
    self.color("white")
    self.penup()
    self.goto(0,270)
    self.update()
    self.hideturtle()
    self.increase()
    
  def update(self):
    self.write(f"Score {self.score} High Score: {self.highScore} ",align="center",font=("Arial",24,"normal"))
    
  def increase(self):
    self.score +=1
    self.clear()
    self.update()
    
  # def gameOver(self):
    # self.goto(0,0)
    # # self.write(f"GAME OVER {self.score}",align="center",font=("Arial",32,"bold"))
    
  def reset(self):
    if self.score > self.highScore:
      self.highScore = self.score
    self.score = 0
    self.clear()
    self.update()