import os
import pandas as pd
from src.utils.customLogger import logger
from src.utils.customException import handle_exceptions
from pathlib import Path


@handle_exceptions
def ensureDbFiles(targetFolder,fileSpecs):
    
    # This function is to check that the database exists or not in the backend,
    # if not then create.

    if not os.path.exists(targetFolder):

        logger.info(f"{Path(__file__).name}: Database not found. Creating...")

        os.makedirs(targetFolder)
    
    logger.info(f"{Path(__file__).name}: Database found. Checking Tables...")

    for fileName,columns in fileSpecs.items():
        filePath=os.path.join(targetFolder,fileName)
        if not os.path.exists(filePath):
            logger.info(f"{Path(__file__).name}: Creating {filePath}...")
            df=pd.DataFrame(columns=columns)
            df.to_excel(filePath,index=False)
        else:
            logger.info(f"{Path(__file__).name}: {filePath} already exists.")

