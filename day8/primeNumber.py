
number = int(input('Enter your number:  '))
def primeNumberCheck(number):
  isPrime = True
  for i in range(2,number - 1):
    if number % i == 0:
      isPrime = False
  if isPrime:
    print(f'The number {number} is a prime number ') 
  else:
    print(f'The number {number} is not a prime number ') 
    
  
primeNumberCheck(number)  