
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
op = input("Enter the one of the following symbols for operation\n + for add , - for sub , * for mul ,/ for div, % for modulo, . for percentage  ")

function = operations[op]
a = function(num1,num2)
print(a)