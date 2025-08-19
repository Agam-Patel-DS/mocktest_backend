
import pandas as pd

def readQuestionData():

  df = pd.read_excel('/content/mock test project.xlsx')
  return df

def questionsBasedOnDifficulty(data:dict, seed=42):
    difficultyLevel=data['params']["difficultyLevel"]
    dataStructure=data["params"]["dataStructure"]
    numberOfQuestions=data["params"]["numberOfQuestions"]


    df=readQuestionData()
    index=[i for i in range(1,numberOfQuestions+1)]
    filteredDf=df[df['level'].isin(difficultyLevel) & df['datastructure'].isin(dataStructure)]
    #filteredDf=filteredDf.head(numberOfQuestions)
    sampleDf=filteredDf.sample(n=min(numberOfQuestions, len(filteredDf)), random_state=seed)
    # questionsForFrontend=dict(zip(filteredDf["id"], filteredDf["question"]))
    # questionsForDatabase=dict(zip(index, questionsForFrontend.keys()))
    questionsForFrontend=dict(zip(sampleDf["id"], sampleDf["question"]))
    questionsForDatabase=dict(zip(index, questionsForFrontend.keys()))
    return questionsForFrontend, questionsForDatabase


def dataFromFrontend():
  data={"userId":"agampatel@gmail.com",
        "testType":"difficultyWise",
        "params":{"difficultyLevel":["easy", "medium"],
                  "dataStructure":["array"],
                  "timeLimit":"None",
                  "company":[],
                  "numberOfQuestions":8,
                  }
  }
  return data

