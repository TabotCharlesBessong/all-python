class QuizBrain: 
  def __init__(self,questionList):
    self.questionNumber = 0
    self.list = questionList
    self.score = 0
    
    
  def stillHasQuestion(self):
    # length = len(self.list)  
    # length -=1
    # if length == 6:
    #   print('You have answered all the questions')
    #   return False
    # else:
    #   return True
    # print(length)
    
    # if self.questionNumber < len(self.list): return True
    # else: return False 
    
    return self.questionNumber < len(self.list)
    
  def nextQuestion(self):
    currentQuestion = self.list[self.questionNumber]
    self.questionNumber += 1
    userAnswer = input(f"Q.{self.questionNumber} : {currentQuestion.text} (True/False) ")
    self.checkAnswer(userAnswer,currentQuestion.answer)
    
  def checkAnswer(self , userAnswer , correctAnswer):
    if userAnswer.lower() == correctAnswer.lower():
      print('You got it right!')
      self.score += 1
    else:
      print('You got it wrong') 
    print(f"Answer is : {correctAnswer} ")  
    print(f"Your current score is : {self.score}/{self.questionNumber} ")
    # print("/day1/input.py")