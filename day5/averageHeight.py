
stdH = input("Input a list of students heights ").split()

totalH = 0
for i in range(0, len(stdH)):
  stdH[i] = int(stdH[i])
  totalH += stdH[i] 

print(stdH)
avgH = totalH / float(len(stdH))  

#  alternatively total height can still be equal to 
#  totalH = sum(stdH)

#  instead of usinf the len function , to build our muscles we could still make use of the for loop to get the len of those values 
numStd = 0
for l in stdH:
  numStd += 1

print(numStd)  
  
print(f'Student average height is  {avgH} ')  