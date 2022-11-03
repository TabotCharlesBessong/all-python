
bill = input('How much is your bill:  ')
tip = input('What percentage tip will you give , 10 , 15, 20:  ')
people = input('How many are splitting this bill:  ')

billFloat = float(bill) 
tipFloat = float(tip)
peopleInt = int(people)

bonus = billFloat * (tipFloat / 100)
newBill = billFloat + bonus
finalBill = newBill / peopleInt
print(f'You are {peopleInt} of you , you tip is {tipFloat}% so it will be divided into ${finalBill} for a total of ${newBill} ')