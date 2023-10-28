
weatherC = {
  "Monday":12,
  "Tuesday":14,
  "wednesday":15,
  "Thursday":14,
  "Friday":21,
  "Saturday":22,
  "Sunday":24
}

weatherF = {temp:((value * 1.8) + 32 ) for (temp,value) in weatherC.items() }
print(weatherF)