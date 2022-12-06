import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
for _ in range(15):
  # move forward by 10 pace
  tim.forward(10)
  # take the pen off the screen
  tim.penup()
  # move forward again as the pen is up
  tim.forward(10)
  # put it down again and the process continues
  tim.pendown()