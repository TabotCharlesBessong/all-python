
import random 

# names = ['Atem','George','Catongo','Will','Solomon']

# val = int(random.seed(len(names)))
# name = names[val]

# print(f' {name} will pay toady"s bill ')

testSeed = int(input('Create a seed number: ')) 
random.seed(testSeed)

# split string method
namesAsCsv = input('Give me everybody"s name , seperated by a comma') 
names = namesAsCsv.split(", ")


x = len(names) - 1
ran = random.randint(0,x)
person = names[ran]
print(ran)
# print(f' {person} will pay the bill ')