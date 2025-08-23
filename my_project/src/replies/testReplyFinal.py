from src.requests.testRequest import testRequestHandler
from src.modules.testReply.testByDifficulty import testByDifficultyGeneration
from src.modules.testReply.testByCompanies import testByCompaniesGeneration
from src.utils.customException import handle_exceptions
from src.config.testReplyConfigManager import testReplyConfigurationManager
from src.modules.database.dbTestReply import databaseQuestionDetailsTestReplyHandler

@handle_exceptions
def testByDifficultyReplyFinal(data:dict):
    requestConfigurationManager=testRequestHandler(data)
    requestConfiguration=requestConfigurationManager.returnConfig()
    testGenerator=testByDifficultyGeneration(requestConfiguration)
    testDict,dbDict=testGenerator.generateTest()
    # Database
    dbdata={
        "userId": data["userId"],
        "testId": data["testId"],
        "questionIds": dbDict,
    }
    if testDict and dbDict:
        dbConfigManager=testReplyConfigurationManager(dbdata)
        dbConfig=dbConfigManager.dataQuestionsDetailsManager()
        db=databaseQuestionDetailsTestReplyHandler(dbConfig)
        db.dbQuestionDetailsInit()
    return testDict, dbDict

@handle_exceptions
def testByCompaniesReplyFinal(data:dict):
    requestConfigurationManager=testRequestHandler(data)
    requestConfiguration=requestConfigurationManager.returnConfig()
    testGenerator=testByCompaniesGeneration(requestConfiguration)
    testDict,dbDict=testGenerator.generateTest()
    # Database
    dbdata={
        "userId": data["userId"],
        "testId": data["testId"],
        "questionIds": dbDict,
    }
    if testDict and dbDict:
        dbConfigManager=testReplyConfigurationManager(dbdata)
        dbConfig=dbConfigManager.dataQuestionsDetailsManager()
        db=databaseQuestionDetailsTestReplyHandler(dbConfig)
        db.dbQuestionDetailsInit()
    return testDict, dbDict