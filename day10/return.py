
def isLeap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
    

def daysInMonth(year,month):
  """Take the year and month and return the number of days in that month for that year considering the leap year"""
  monthDays = [31,28,31,30,31,30,31,31,30,31,30,31] 
  if isLeap(year):
    monthDays[1] = 29
  # index = monthDays.index(month)   
  index = month - 1
  
  days = monthDays[index]  
  return days
year = int(input("Enter a year: ")) 
month = int(input("Enter a month: ")) 
days = daysInMonth(year,month)          
print(f'There are {days} in this month ')        