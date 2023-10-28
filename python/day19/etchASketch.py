
from turtle import Turtle , Screen 

tom = Turtle()
screen = Screen()

def moveForward():
  tom.forward(15)
  
def moveBackward():
  tom.backward(15)
  
def moveCounterClock():
  tom.left(10)
  # newHeading = tom.heading() + 10
  # tom.setheading(newHeading)
  tom.forward(15)
  
def moveClock():
  tom.right(10)
  # newHeading = tom.heading() - 10
  # tom.setheading(newHeading)
  tom.forward(15)
  
def clear():
  # clear the turtle but keeps it at his it position
  # tom.clear()
  # clear the turtle and brings it back to its starting point 
  tom.reset()
  # pass
  
# direction = input("Enter W to move forward, S to move backwards , A to move left , D to move right").lower()
  
# def move(func):
#   if direction == 'w':
#     func = moveForward()
#     return func
#   elif direction == 's':
#     func = moveBackward()
#     return func
#   elif direction == 'a':
#     func = moveCounterClock()
#     return func
#   elif direction == 'd':
#     func = moveClock()
#     return func
#   else:
#     screen.exitonclick()
#   return func

  
screen.listen()
screen.onkey(key="w",fun=moveForward)  
screen.onkey(key="s",fun=moveBackward)  
screen.onkey(key="a",fun=moveCounterClock)  
screen.onkey(key="d",fun=moveClock)  
screen.onkey(key="c",fun=clear)  
screen.exitonclick()