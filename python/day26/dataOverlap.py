
with open(r"day26\t1.txt") as file1:
  d1 = file1.readlines()

with open(r"day26\t2.txt") as file2:
  d2 = file2.readlines()  
  
result = [int(newItem) for newItem in d1 if newItem in d2]
print(result)