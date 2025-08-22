from src.utils import readData
from src.entity.testReplyConfigs import testByDifficultyConfig

class testByDifficultyGeneration:
    def __init__(self,data:testByDifficultyConfig):
        self.data=data

    def generateTest(self):
        numberOfQuestions=self.data.numberOfQuestions
        difficultyLevel=self.data.difficultyLevel
        dataStructure=self.data.dataStructure
        excelPath=self.data.excelPath
        seed=self.data.seed

        df=readData(excelPath)

        index=[i for i in range(1,numberOfQuestions+1)]

        filteredDf=df[df['difficulty'].isin(difficultyLevel) & df['dataStructure'].isin(dataStructure)]

        sampleDf=filteredDf.sample(n=min(numberOfQuestions, len(filteredDf)), random_state=seed)
        questionsForFrontend=dict(zip(sampleDf["id"], sampleDf["question"]))
        questionsForDatabase=dict(zip(index, questionsForFrontend.keys()))

        return questionsForFrontend, questionsForDatabase

    