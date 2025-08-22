import pandas as pd

target="db"

filesAndColumns = {
   "testUserDetails.xlsx":["userId","testId","testType"],
   "testDetails.xlsx":["userId","testId","numberOfQuestions","difficultyLevel","companies","dataStructure","timeLimit"],
   "questionDetails.xlsx":["userId","testId","questionIds"],
   "solutionDetails.xlsx":["userId","testId","solutions","timeTaken"],
   "scoreDetails.xlsx":["userId","testId","result","score"]
}   

def readData(datapath:str):

  df = pd.read_excel(datapath)
  return df

import yaml
from types import SimpleNamespace

def loadConfig(config):
  with open(config, "r") as f:
      data=yaml.safe_load(f)

  def dictToNamespace(d):
    if isinstance(d,dict):
       return SimpleNamespace(**{k:dictToNamespace(v) for k,v in d.items()})
    elif isinstance(d,list):
       return [dictToNamespace(i) for i in d]
    else:
       return d
    
  return dictToNamespace(data)
      


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
        "testId":12356442,
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
