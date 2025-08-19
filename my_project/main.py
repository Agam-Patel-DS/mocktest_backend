


from src.modules.testReply.testReplyFinal import testReplyFinal
from src.utils import returnDemoDataByDifficulty
from src.utils.customLogger import logger

logger.info("Logger Initialised")
data=returnDemoDataByDifficulty()
logger.info(f"Request Data From User: {data}")
reply=testReplyFinal(data)
logger.info(f"Code Complete")
print(reply)