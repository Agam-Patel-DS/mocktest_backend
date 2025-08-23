from src.entity.testReplyConfigs import testByDifficultyConfig, testByCompaniesConfig, testByGenAIConfig, databaseTestDetailsConfig, databaseTestInitConfig, databaseQuestionDetailsConfig
from src.utils.customException import handle_exceptions
from src.utils.customLogger import logger
from pathlib import Path


class testReplyConfigurationManager:
    def __init__(self,data:dict):
        
        # This class returns all the configurations required for testReply Module

        logger.info(f"{Path(__file__).name}: running testReplyConfigurationManager")

        self.data=data

    # Configuration for testByDifficulty
    def testByDifficultyConfiguration(self):

        logger.info(f"{Path(__file__).name}: making testByDufficultyConfiguration")

        config=testByDifficultyConfig(
            dataStructure=self.data["params"]["dataStructure"],
            difficultyLevel=self.data["params"]["difficultyLevel"],
            numberOfQuestions=self.data["params"]["numberOfQuestions"],
            seed=self.data["params"]["seed"],
            excelPath="data/questions.xlsx"
        )
        return config
    
    # Configuration for testByCompanies
    def testByCompaniesConfiguration(self):

        logger.info(f"{Path(__file__).name}: making testByCompaniesConfiguration")

        config=testByCompaniesConfig(
            difficultyLevel=self.data["params"]["difficultyLevel"],
            companies=self.data["params"]["companies"],
            numberOfQuestions=self.data["params"]["numberOfQuestions"],
            excelPath="data/questions.xlsx",
            seed=self.data["params"]["seed"]
        )
        return config

    # Configuration for testByGenAI
    def testByGenAIConfiguration(self):

        logger.info(f"{Path(__file__).name}: making testByGenAIConfiguration")

        config=testByGenAIConfig(
            difficultyLevel=self.data["params"]["difficultyLevel"],
            numberOfQuestions=self.data["params"]["companies"],
            dataStructure=self.data["params"]["dataStructure"]
        )

    # Configuration for databaseTestInit
    def databaseTestInitManager(self):

        logger.info(f"{Path(__file__).name}: making databaseTestInitManager Configuration")

        config=databaseTestInitConfig(
            userId=self.data["userId"],
            testId=self.data["testId"],
            testType=self.data["testType"],
            timeStamp=self.data["timeStamp"]
        )
        return config
    
    # Configuration for databaseTestDetails
    def databaseTestDetailsManager(self):

        logger.info(f"{Path(__file__).name}: making databaseTestDetailsManager Configguration")

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
    
    # Configuration for databaseQuestionDetails
    def dataQuestionsDetailsManager(self):

        logger.info(f"{Path(__file__).name}: making dataQuestionsDetailsManager Configuration")

        config=databaseQuestionDetailsConfig(
            userId=self.data["userId"],
            testId=self.data["testId"],
            questionIds=self.data["questionIds"],
        )
        return config