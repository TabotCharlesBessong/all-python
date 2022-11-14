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
    input(f"Q.{self.questionNumber} : {currentQuestion.text} (True/False) ")
    
  def checkAnswer(self):
    pass