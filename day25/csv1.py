
import csv
import pandas as pd

with open(r"day25\weatherData.csv") as data:
  d = csv.reader(data)
  temperatures = []
  for row in d:
    if row[1] != 'temp':
      intTemp = int(row[1])
      temperatures.append(intTemp)
  print(temperatures)
  
dt = pd.read_csv("day25\weatherData.csv")
print(dt)