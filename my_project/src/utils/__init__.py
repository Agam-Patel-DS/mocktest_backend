import pandas as pd
from datetime import datetime


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
      
ts=datetime.now()

def returnDemoDataByDifficulty():
    data={
       "userId":"agampatel@gmail.com",
        "testType":"testByDifficulty",
        "timeStamp": ts.strftime("%Y-%m-%d %H:%M:%S"),
        "params":{
                  "difficultyLevel":["easy", "medium"],
                  "dataStructure":["array", "string"],
                  "companies":[],
                  "timeLimit":"None",
                  "numberOfQuestions":8,
                  "seed":48,
                  }
    }
    return data


def returnDemoDataByCompanies():
    data={
       "userId":"agampatel@gmail.com",
        "testId":12356442,
        "testType":"testByCompanies",
        "timeStamp": ts.strftime("%Y-%m-%d %H:%M:%S"),
        "params":{
                  "difficultyLevel":["easy", "medium"],
                  "dataStructure":[],
                  "companies":["Flipkart", "Amazon"],
                  "timeLimit":"None",
                  "numberOfQuestions":8,
                  "seed":48,
                  }
    }
    return data
