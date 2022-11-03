

height = input('What is your height in m:  ')
weight = input('What is your weight in kg: ')

bmi = int(weight) / float(height) ** 2
print('Your body mass index is :',int(bmi))

if bmi < 18.5:
  print(f' your bmi is {bmi} and you are underweight ')
elif (bmi > 18.5 and bmi < 25 ):
  print('f your bmi is {bmi} and you are normal weight ')
elif (bmi > 25 and bmi < 30 ):
  print('f your bmi is {bmi} and you are over weight ')
elif (bmi > 30 and bmi < 35 ):
  print('f your bmi is {bmi} and you are obese ')
else:
  print('f your bmi is {bmi} and you are clinicaly obese ')