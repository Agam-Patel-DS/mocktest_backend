from src.requests.testRequest import testRequestHandler
from src.modules.testReply.testByDifficulty import testByDifficultyGeneration
from src.modules.testReply.testByCompanies import testByCompaniesGeneration
from src.utils.customException import handle_exceptions
from src.config.testReplyConfigManager import testReplyConfigurationManager
from src.modules.database.dbTestReply import databaseQuestionDetailsTestReplyHandler
from src.utils.customLogger import logger
from pathlib import Path

@handle_exceptions
def testByDifficultyReplyFinal(data:dict):

    # Getting configuration
    logger.info(f"{Path(__file__).name}: testByDifficultyReplyFinal called")

    requestConfigurationManager=testRequestHandler(data)
    requestConfiguration=requestConfigurationManager.returnConfig()

    # Generating the test
    logger.info(f"{Path(__file__).name}: generating test...")

    testGenerator=testByDifficultyGeneration(requestConfiguration)
    testDict,dbDict=testGenerator.generateTest()

    logger.info(f"{Path(__file__).name}: test generated")

    # Database - saving the question ids in the database
    dbdata={
        "userId": data["userId"],
        "testId": data["testId"],
        "questionIds": dbDict,
    }

    if testDict and dbDict:
        
        # If there are no duplicate enteries then
        dbConfigManager=testReplyConfigurationManager(dbdata)
        dbConfig=dbConfigManager.dataQuestionsDetailsManager()

        logger.info(f"{Path(__file__).name}: saving question ids in the database")

        db=databaseQuestionDetailsTestReplyHandler(dbConfig)
        db.dbQuestionDetailsInit()

        logger.info(f"{Path(__file__).name}: question ids saved in the database")

    return testDict, dbDict

@handle_exceptions
def testByCompaniesReplyFinal(data:dict):
    
    # Getting configuration
    logger.info(f"{Path(__file__).name}: testByCompaniesReplyFinal called")

    requestConfigurationManager=testRequestHandler(data)
    requestConfiguration=requestConfigurationManager.returnConfig()

    # Generating test
    logger.info(f"{Path(__file__).name}: generating test...")

    testGenerator=testByCompaniesGeneration(requestConfiguration)
    testDict,dbDict=testGenerator.generateTest()

    logger.info(f"{Path(__file__).name}: test generated")

    # Database - saving question ids in the database
    dbdata={
        "userId": data["userId"],
        "testId": data["testId"],
        "questionIds": dbDict,
    }

    if testDict and dbDict:

        # If there are no duplicate enteries in the database
        dbConfigManager=testReplyConfigurationManager(dbdata)
        dbConfig=dbConfigManager.dataQuestionsDetailsManager()

        logger.info(f"{Path(__file__).name}: saving the question ids in the database")

        db=databaseQuestionDetailsTestReplyHandler(dbConfig)
        db.dbQuestionDetailsInit()

        logger.info(f"{Path(__file__).name}: question ids saved in the database")
        
    return testDict, dbDict