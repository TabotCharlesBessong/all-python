
dictionary = {"name":"Charles","height":1.78,"age":20,"sex":"male"}

print(dictionary["name"])

# creating an empty dictionary 
emptyDictoinary = {}

# wipping out an existing dictionary
# dictionary = {}

# editing an item in a dictionary 
# if the value does not exist , it wil create a new value
dictionary["name"] = "Tabot charles"
print(dictionary)

# adding an item in the dictionary 
dictionary["role"] = "developer"
print(dictionary)

# looping through a dictionary 
for key in dictionary:
  print(dictionary[key])