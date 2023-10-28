
from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def moveForward():
  tom.forward(10)
  
screen.listen()
screen.onkey(key="space",fun=moveForward)  
screen.exitonclick()