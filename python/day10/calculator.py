
from art import logo 

print(logo)

def add(n1,n2):
  return n1 + n2

def sub(n1,n2):
  return n1 - n2

def mul(n1,n2):
  return n1 * n2

def div(n1,n2):
  return n1 / n2

def mod(n1,n2):
  return n1 % n2

def perct(n1,n2):
  n3 = div(n1,n2)
  p = mul(n3,100)
  return p

# The dictionary will be used to map the functions thanks to their keys 
operations = {
  "+":add,
  "-":sub,
  "*":mul,
  "/":div,
  "%":mod,
  ".":perct
}


num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# The value we are taking here is the key to the operations dictionary so that they will map the functions to their names 
# Take not the values must be same as that of the function 
op = input("Enter the one of the following symbols for operation\n + for add , - for sub , * for mul ,/ for div, % for modulo, . for percentage  ")

# The function has already been called and just need to be passed to a value
function = operations[op]
a = function(num1,num2)
print(a)
