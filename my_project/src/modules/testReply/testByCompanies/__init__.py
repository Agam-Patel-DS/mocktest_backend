from src.utils import readData
import pandas as pd
import numpy as np
from src.entity.testReplyConfigs import testByCompaniesConfig

class testByCompaniesGeneration:
    def __init__(self,data:testByCompaniesConfig):
        self.data=data

    def generateTest(self):
        numberOfQuestions=self.data.numberOfQuestions
        difficultyLevel=self.data.difficultyLevel
        companies=self.data.companies
        excelPath=self.data.excelPath
        seed=self.data.seed

        df=readData(excelPath)

        index=[i for i in range(1,numberOfQuestions+1)]

        df=df[df['difficulty'].isin(difficultyLevel)]
        companies_lower=[c.lower().strip() for c in companies]
        df['companies_lower']=df['companies'].str.lower().str.split(',').apply(lambda x: [item.strip() for item in x])
        df=df[df['companies_lower'].apply(lambda x: any(comp in x for comp in companies_lower))]
        df=df.drop(columns=['companies_lower'])
        np.random.seed(seed)
        sampleDf=df.sample(n=numberOfQuestions)
        print(sampleDf['companies'])
        questionsForFrontend=dict(zip(sampleDf["id"], sampleDf["question"]))
        questionsForDatabase=dict(zip(index, questionsForFrontend.keys()))

        return questionsForFrontend, questionsForDatabase

    