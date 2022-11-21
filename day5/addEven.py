
total = 0

for i in range(1,101):
  if i % 2 == 0:
    total += i
    
print (f'The total is {total}') 

  #  alternatively
total2 = 0
for n in range(2,201,2):
  # print(n)   
  total2 += n
print(total2)   