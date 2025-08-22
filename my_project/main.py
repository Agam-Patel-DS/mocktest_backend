


from src.replies.testReplyFinal import testByCompaniesReplyFinal
from src.utils import returnDemoDataByCompanies
from src.utils.customLogger import logger

logger.info("Logger Initialised")
data=returnDemoDataByCompanies()
logger.info(f"Request Data From User: {data}")
reply=testByCompaniesReplyFinal(data)
logger.info(f"Code Complete")
print(reply)