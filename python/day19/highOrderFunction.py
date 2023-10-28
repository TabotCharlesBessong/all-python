
def add(n1,n2):
  return n1 + n2

def sub(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

def calculator(n1,n2,func):
  return func(n1,n2)
  
print(calculator(2,6,divide))