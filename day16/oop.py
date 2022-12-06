
# import turtle as turtle 
from turtle import Turtle , Screen

tommy = Turtle()
print(tommy)
tommy.shape('turtle')
tommy.color('blue')
tommy.forward(distance=100)

myScreen = Screen()
h = myScreen.canvheight
w = myScreen.canvwidth
print(h,w)
myScreen.exitonclick()