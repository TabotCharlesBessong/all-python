
import random

celebrity = [
  {
    "name":"Rihana",
    "followers":340
  },
  {
    "name":"Eto'o",
    "followers":230
  },
  {
    "name":"Messi",
    "followers":560
  },
  {
    "name":"Ronaldo",
    "followers":830
  },
  {
    "name":"Beyonce",
    "followers":190
  },
  {
    "name":"Neymar",
    "followers":390
  },
]

a = random.choice(celebrity)
b = random.choice(celebrity)
if a == b :
  b = random.choice(celebrity)
  
nameA = a["name"]
nameB = b["name"]    
print(nameA,nameB) 
guess = input(f"Who do you think has more instagram followers {nameA} or {nameB}\nTake a for {nameA} and b for {nameB}:  ")

def compare(a,b):
  if a["followers"] > b["followers"]:
    print( f"{nameA} has more instagram followers than {nameB}"  ) 
  elif a["followers"] < b["followers"]:
    print( f"{nameB} has more instagram followers than {nameA}"  )
  else:
    print("There are equal")
compare(a,b)   