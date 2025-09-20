from src.config.scoreReplyConfigManager import scoreReplyConfigurationManager
from src.modules.tests.test_main import testHandler



def scoreReplyFinalForAll(data:dict):
  configManager=scoreReplyConfigurationManager(data)
  config=configManager.solutionDetailsConfigurationManager()
  testHandlerObj=testHandler(config)
  finalResult=testHandlerObj.returnResult()
  # Database
  return finalResult