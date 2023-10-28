
country = input("What country have you been to?: ")
visits = int(input("How many times have you been there: "))
cities = input("Enter the cities you have been to separated with a ,: ").split()

travelLog = [
  {
    "country":"France",
    "visits":12,
    "cities":["Paris","Lille","Dijon"]
  },
  {
    "country":"Germany",
    "visits":5,
    "cities":["Berlin","Hamburg","Stuttgart"]
  }
]

print(travelLog)

def newTravelLog(count,vis,cit):
  newDict = {"country":count, "visits":vis , "cities":cit}
  travelLog.append(newDict)
  l = len(travelLog)
  print(travelLog)
  print(travelLog[l-1])
  
newTravelLog(count=country , vis = visits , cit=cities)  