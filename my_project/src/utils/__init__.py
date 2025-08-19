import pandas as pd

def readData(datapath:str):

  df = pd.read_excel(datapath)
  return df


def returnDemoDataByDifficulty():
    data={"userId":"agampatel@gmail.com",
        "testType":"testByDifficulty",
        "params":{"difficultyLevel":["easy", "medium"],
                  "dataStructure":["array", "string"],
                  "timeLimit":"None",
                  "company":[],
                  "numberOfQuestions":8,
                  }
    }
    return data
