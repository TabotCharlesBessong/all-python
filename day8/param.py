
def greet(name):
  print(f'Hello {name} how are you doing')
  
name = input('Whats your name?: ')
location = input('Where are you from?: ')
# greet(nom)  

# positional vs keyword arguments
def greetWith(name,location):
  print(f'Hello everyone , meet {name} \n He is from {location} ')
  

# positional arguments  
greetWith(location,name)  
# greetWith(nom,location)  

#  keyword argument 
greetWith(location='Germany',name='Einstein')
  