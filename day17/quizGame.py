
from data import question_data
from quizModel import Question
from quizBrain import QuizBrain

questionBank = []

for question in question_data:
  questionText = question['text']
  questionAnswer = question['answer']
  newQuestion = Question(questionText,questionAnswer)
  questionBank.append(newQuestion)
  

quiz = QuizBrain(questionBank)

# quiz.nextQuestion() 
# print(quiz.stillHasQuestion())

while quiz.stillHasQuestion():
  # print(quiz.stillHasQuestion())
  quiz.nextQuestion()
# print(questionBank)