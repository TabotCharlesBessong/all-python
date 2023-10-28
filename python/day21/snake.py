
from turtle import Turtle, up



STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  
  def __init__(self):
    self.segments = []
    self.createSnake()
    self.head = self.segments[0]
  
  def createSnake(self):
    for pos in STARTING_POSITION:
      self.addSegment(pos)
      
  def move(self):
    for i in range(len(self.segments) - 1,0,-1):
      newX = self.segments[i - 1].xcor()
      newY = self.segments[i - 1].ycor()
      self.segments[i].goto(newX,newY)
    self.head.forward(MOVE_DISTANCE)
  
  def addSegment(self,pos):
    newSegment = Turtle(shape='square')
    newSegment.color('white')
    newSegment.penup()
    newSegment.goto(pos)
    self.segments.append(newSegment)
    
  def reset(self):
    for seg in self.segments:
      seg.goto(1000,1000)
    self.segments.clear()
    self.createSnake()
    self.head = self.segments[0]
  def extend(self):
    self.addSegment(self.segments[-1].position())
      
  def up(self):
    if self.head.heading() != DOWN:
      self.segments[0].setheading(UP)
  
  def down(self):
    if self.head.heading() != UP:
      self.segments[0].setheading(DOWN)
  
  def left(self):
    if self.head.heading() != RIGHT:
      self.segments[0].setheading(LEFT)
  
  def right(self):
    if self.head.heading() != LEFT:
      self.segments[0].setheading(RIGHT)
  # segments[0].left(90)