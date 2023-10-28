
name = "Charles"
list = [letter for letter in name]
print(list)
scores = [89,56,76,89,86,67]
score = [s for s in scores]
print(score)

evenScores = [m for m in range(1,101) if m % 2 == 0]
print(evenScores)

# operation with list
rangeList = [num **2 for num in range(0,20)]
print(rangeList)

# conditional comprehension

people = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie","Dan"]
# shortPeople = [len(name) <= 4 for name in people]
shortPeople = [name for name in people if len(name)<=4]
# converting all names in the list to uppercase using list comprehension 
upperPeople = [name.upper() for name in people ]
shortUpperPeople = [name.upper() for name in people if len(name)<=4]
print(shortPeople)
print(upperPeople)
print(shortUpperPeople)