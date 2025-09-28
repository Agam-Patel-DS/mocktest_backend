import os
from src.entity.scoreReplyConfigs import solutionDetailsConfig
from src.modules.sidereq.retrieveQuestions import get_questions_from_excel
from src.modules.tests.testGenAI import evaluate_all, count_correct_solutions
from src.modules.database.dbDetails import generalRetrieval

class testHandler:
  def __init__(self,config:solutionDetailsConfig):
    self.config=config
    print(f"userId: {self.config.userId}, testId: {self.config.testId}")
    self.dbret=generalRetrieval(self.config.userId, self.config.testId)
    self.testDetails=self.dbret.get_test_details()
    print(f"testDetails: {self.testDetails}")
    self.questionIds=self.dbret.retrieveQuestionIdsGeneral()

  def testbyAI(self):
   
    if self.testDetails["testType"]!="testByGenAI":
      questions=get_questions_from_excel(self.config.excelPath, self.config.solutions.keys())
    else:
      questions=self.questionIds
    
    print(f"Questions: {questions}")
    solutions=self.config.solutions
    print(solutions)
    result=evaluate_all(questions, solutions)
    correctCount=count_correct_solutions(result)
    return result, correctCount

  def returnResult(self):
    result,correctCount=self.testbyAI()
    finalReply={"result":result, "correctCount":correctCount, "timeTaken":self.config.timeTaken, "testDetails":self.testDetails}
    return finalReply


  
