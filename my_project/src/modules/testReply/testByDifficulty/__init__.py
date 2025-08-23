from src.utils import readData
from src.entity.testReplyConfigs import testByDifficultyConfig
from src.utils.customException import handle_exceptions
from src.utils.customLogger import logger
from pathlib import Path

class testByDifficultyGeneration:

    # This module will generate the test for the testByDifficulty or testByDataStructure Module

    def __init__(self,data:testByDifficultyConfig):

        logger.info(f"{Path(__file__).name}: test by difficuly generation...")

        self.data=data

    @handle_exceptions
    def generateTest(self):

        if self.data==None:

            logger.info(f"{Path(__file__).name}: duplicates found")

            return None, None

        numberOfQuestions=self.data.numberOfQuestions
        difficultyLevel=self.data.difficultyLevel
        dataStructure=self.data.dataStructure
        excelPath=self.data.excelPath
        seed=self.data.seed
        
        logger.info(f"{Path(__file__).name}: Parameter: noq: {numberOfQuestions}, diff: {difficultyLevel}, DSA:{dataStructure}, seed:{seed}")

        df=readData(excelPath)

        index=[i for i in range(1,numberOfQuestions+1)]

        filteredDf=df[df['difficulty'].isin(difficultyLevel) & df['dataStructure'].isin(dataStructure)]

        sampleDf=filteredDf.sample(n=min(numberOfQuestions, len(filteredDf)), random_state=seed)
        questionsForFrontend=dict(zip(sampleDf["id"], sampleDf["question"]))
        questionsForDatabase=dict(zip(index, questionsForFrontend.keys()))

        logger.info(f"{Path(__file__).name}: questions found, returning dictionaries...")

        return questionsForFrontend, questionsForDatabase

    