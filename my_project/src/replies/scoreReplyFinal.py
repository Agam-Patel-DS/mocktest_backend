from src.config.scoreReplyConfigManager import scoreReplyConfigurationManager
from src.modules.tests.test_main import testHandler
from src.utils.customLogger import logger


def scoreReplyFinalForAll(data:dict):
  configManager=scoreReplyConfigurationManager(data)
  logger.info(f"data: {data}")
  config=configManager.solutionDetailsConfigurationManager()
  testHandlerObj=testHandler(config)
  finalResult=testHandlerObj.returnResult()
  # Database
  return finalResult