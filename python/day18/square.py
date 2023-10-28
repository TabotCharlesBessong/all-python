import turtle as t

timmy_the_turtle = t.Turtle()

for _ in range(6):
    # move forward by 10 pace
    timmy_the_turtle.forward(100)
    # turn left after every 100 pace
    timmy_the_turtle.left(60)
    # turning left continuously will lead to a square
    
    # if we had desire of drawing a triangle , it would have been by a range of 3 and turning left 120deg
    