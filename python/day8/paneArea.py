
import math

testH = int(input('What is the height of the wall?: '))
testW = int(input('What is the width of the wall?: '))
coverage = 5

area = 0
canNumber = 0

def paneArea(h  , w  , cover ):
  area = h * w
  canNumber = math.ceil(area / cover)
  print(f"The surface area of the room is {area} and we will need {canNumber} to pain the room ")
  
paneArea(w = testW, cover = coverage, h = testH)  