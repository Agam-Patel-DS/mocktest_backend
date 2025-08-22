from src.entity.testReplyConfigs import testByDifficultyConfig, testByCompaniesConfig, testByGenAIConfig

class testReplyConfigurationManager:
    def __init__(self,data:dict):
        self.data=data

    def testByDifficultyConfiguration(self):
        config=testByDifficultyConfig(
            dataStructure=self.data["params"]["dataStructure"],
            difficultyLevel=self.data["params"]["difficultyLevel"],
            numberOfQuestions=self.data["params"]["numberOfQuestions"],
            seed=self.data["params"]["seed"],
            excelPath="data/questions.xlsx"
        )
        return config
    
    def testByCompaniesConfiguration(self):
        config=testByCompaniesConfig(
            difficultyLevel=self.data["params"]["difficultyLevel"],
            companies=self.data["params"]["companies"],
            numberOfQuestions=self.data["params"]["numberOfQuestions"],
            excelPath="data/questions.xlsx",
            seed=self.data["params"]["seed"]
        )
        return config

    def testByGenAIConfiguration(self):
        config=testByGenAIConfig(
            difficultyLevel=self.data["params"]["difficultyLevel"],
            numberOfQuestions=self.data["params"]["companies"],
            dataStructure=self.data["params"]["dataStructure"]
        )