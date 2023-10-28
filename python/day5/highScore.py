
scores = input('Enter scores for the test:\n').split()

for n in range(0 , len(scores)):
  scores[n] = int(scores)
print(scores)  

hScore = 0
for score in scores: 
  if score > hScore:
    hScore = score
print(f"The highest score is {hScore} ")    