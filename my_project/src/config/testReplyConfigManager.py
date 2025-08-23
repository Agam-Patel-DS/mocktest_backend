from src.entity.testReplyConfigs import testByDifficultyConfig, testByCompaniesConfig, testByGenAIConfig, databaseTestDetailsConfig, databaseTestInitConfig, databaseQuestionDetailsConfig

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

    def databaseTestInitManager(self):
        config=databaseTestInitConfig(
            userId=self.data["userId"],
            testId=self.data["testId"],
            testType=self.data["testType"],
            timeStamp=self.data["timeStamp"]
        )
        return config
    
    def databaseTestDetailsManager(self):
        config=databaseTestDetailsConfig(
            userId=self.data["userId"],
            testId=self.data["testId"],
            numberOfQuestions=self.data["params"]["numberOfQuestions"],
            companies=self.data["params"]["companies"],
            dataStructures=self.data["params"]["dataStructure"],
            difficultyLevel=self.data["params"]["difficultyLevel"],
            timeLimit=self.data["params"]["timeLimit"],
        )
        return config
    
    def dataQuestionsDetailsManager(self):
        config=databaseQuestionDetailsConfig(
            userId=self.data["userId"],
            testId=self.data["testId"],
            questionIds=self.data["questionIds"],
        )
        return config