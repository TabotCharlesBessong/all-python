
def calculate(n,**kwargs):
  print(kwargs)
  n += kwargs["add"]
  n *= kwargs["multiply"]
  print(n)

calculate(7,add=3,multiply=5)

class Car:
  def __init__(self,**kw):
    self.make = kw["make"]
    self.model = kw["model"]
    
meinAuto = Car(make="Nissan",model="Jtx")
print(meinAuto.model)