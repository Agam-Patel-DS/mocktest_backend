from src.utils import readData
import pandas as pd
import numpy as np
from src.entity.testReplyConfigs import testByCompaniesConfig
from src.utils.customException import handle_exceptions
from src.utils.customLogger import logger
from pathlib import Path

class testByCompaniesGeneration:

    # This module finds questinos for test by companies module

    def __init__(self,data:testByCompaniesConfig):

        logger.info(f"{Path(__file__).name}: generating test by companies...")

        self.data=data
        
    @handle_exceptions
    def generateTest(self):
        if self.data==None:

            logger.info(f"{Path(__file__).name}: duplicates found")

            return None, None

        numberOfQuestions=self.data.numberOfQuestions
        difficultyLevel=self.data.difficultyLevel
        companies=self.data.companies
        excelPath=self.data.excelPath
        seed=self.data.seed

        logger.info(f"{Path(__file__).name}: Parameter: noq: {numberOfQuestions}, diff: {difficultyLevel}, comp: {companies}, seed: {seed}")

        df=readData(excelPath)

        index=[i for i in range(1,numberOfQuestions+1)]

        df=df[df['difficulty'].isin(difficultyLevel)]
        companies_lower=[c.lower().strip() for c in companies]

        df['companies_lower']=df['companies'].str.lower().str.split(',').apply(lambda x: [item.strip() for item in x])
        df=df[df['companies_lower'].apply(lambda x: any(comp in x for comp in companies_lower))]

        df=df.drop(columns=['companies_lower'])
        np.random.seed(seed)

        sampleDf=df.sample(n=numberOfQuestions)
    
        questionsForFrontend=dict(zip(sampleDf["id"], sampleDf["question"]))
        questionsForDatabase=dict(zip(index, questionsForFrontend.keys()))

        logger.info(f"{Path(__file__).name}: Found questions, now returning...")

        return questionsForFrontend, questionsForDatabase

    