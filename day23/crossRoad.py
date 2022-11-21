import time
from turtle import Screen
from player import Player
from carManager import CarManager
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.goUp, "Up")

gameIsOn = True
while gameIsOn:
  time.sleep(0.1)
  screen.update()

  carManager.createCar()
  carManager.moveCars()

  #Detect collision with car
  for car in carManager.allCars:
    if car.distance(player) < 20:
      gameIsOn = False
      scoreboard.gameOver()

  #Detect successful crossing
  if player.isAtFinishLine():
      player.goToStart()
      carManager.levelUp()
      scoreboard.increaseLevel()


screen.exitonclick()