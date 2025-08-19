from src.modules.testReply.testRequest import testRequestHandler
from src.modules.testReply.testByDifficulty import testByDifficultyGeneration
from src.utils.customException import handle_exceptions

@handle_exceptions
def testReplyFinal(data:dict):
    requestConfigurationManager=testRequestHandler(data)
    requestConfiguration=requestConfigurationManager.returnConfig()
    testGenerator=testByDifficultyGeneration(requestConfiguration)
    testDict,dbDict=testGenerator.generateTest()
    return testDict, dbDict