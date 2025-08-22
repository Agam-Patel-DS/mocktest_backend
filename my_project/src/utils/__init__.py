import pandas as pd

def readData(datapath:str):

  df = pd.read_excel(datapath)
  return df


def returnDemoDataByDifficulty():
    data={
       "userId":"agampatel@gmail.com",
        "testType":"testByDifficulty",
        "params":{
                  "difficultyLevel":["easy", "medium"],
                  "dataStructure":["array", "string"],
                  "timeLimit":"None",
                  "numberOfQuestions":8,
                  "seed":48
                  }
    }
    return data


def returnDemoDataByCompanies():
    data={
       "userId":"agampatel@gmail.com",
        "testId":12345242,
        "testType":"testByCompanies",
        "params":{
                  "difficultyLevel":["easy", "medium"],
                  "companies":["Flipkart", "Amazon"],
                  "timeLimit":"None",
                  "numberOfQuestions":8,
                  "seed":48
                  }
    }
    return data
