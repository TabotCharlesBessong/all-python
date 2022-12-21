############DEBUGGING#####################

# # Describe Problem
# The initial value of condition was 21 , 
/* we all know that the range method is exclusive , so it will stop at 20 , the initial value of 21 , the print function will never be exercuted as the condition will forever remain false */
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#     if i == 21:
      
#       print("You got it")
# my_function()

# # Reproduce the Bug
# So errors happens ones out of many times and these bugs are very dangerous as they can cause a product to be shippeed with bugs 
# So running the program many times and checking the function again everytime an error takes place is important so to really find the misterious bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])

# # Play Computer
# some errors are hard to find that you have to read to code line by line 

# I recommend moving to python3.11 as it shows you the exact expression that produced the error and not just the line as in 3.10 and 3.09 
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
  # print("You are a millenial.")
# elif year >= 1994:
  # print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
  # print("You can drive at age {age}.")

# #Print is Your Friend
# printing some of oyur lines can help you display the error in the console
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
