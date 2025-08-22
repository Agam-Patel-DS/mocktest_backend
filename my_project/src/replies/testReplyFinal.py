from src.requests.testRequest import testRequestHandler
from src.modules.testReply.testByDifficulty import testByDifficultyGeneration
from src.modules.testReply.testByCompanies import testByCompaniesGeneration
from src.utils.customException import handle_exceptions

@handle_exceptions
def testByDifficultyReplyFinal(data:dict):
    requestConfigurationManager=testRequestHandler(data)
    requestConfiguration=requestConfigurationManager.returnConfig()
    testGenerator=testByDifficultyGeneration(requestConfiguration)
    testDict,dbDict=testGenerator.generateTest()
    return testDict, dbDict

@handle_exceptions
def testByCompaniesReplyFinal(data:dict):
    requestConfigurationManager=testRequestHandler(data)
    requestConfiguration=requestConfigurationManager.returnConfig()
    testGenerator=testByCompaniesGeneration(requestConfiguration)
    testDict,dbDict=testGenerator.generateTest()
    return testDict, dbDict