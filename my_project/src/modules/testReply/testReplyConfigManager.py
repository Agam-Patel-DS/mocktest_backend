from src.modules.testReply.testReplyConfigs import testByDifficultyConfig

class testReplyConfigurationManager:
    def __init__(self,data:dict):
        self.data=data

    def testByDifficultyConfiguration(self):
        config=testByDifficultyConfig(
            dataStructure=self.data["params"]["dataStructure"],
            difficultyLevel=self.data["params"]["difficultyLevel"],
            numberOfQuestions=self.data["params"]["numberOfQuestions"],
            seed=96,
            excelPath="data/questions.xlsx"
        )
        return config