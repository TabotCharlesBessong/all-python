
from turtle import Turtle , Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title('Nokia 3301 snake game')
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up,key='Up')
screen.onkey(snake.down,key='Down')
screen.onkey(snake.left,key='Left')
screen.onkey(snake.right,key='Right')

# snake.createSnake()
  
# screen.update()  

gameIsOn = True
while gameIsOn:
  screen.update()  
  time.sleep(0.25) 
  
  snake.move()

screen.exitonclick()