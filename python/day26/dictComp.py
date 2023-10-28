
import random
# studentScores = {
#   'Alex':89,
#   'Bath':65
# }

from tkinter.font import names


people = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie","Dan"]

# studentScores = [score for score in names random.randint(1,100) ]
studentScores = {student:random.randint(1,100) for student in people}
passedScores = {student:student for(student,score) in studentScores.items() if score < 61 }
print(studentScores)
print(passedScores)