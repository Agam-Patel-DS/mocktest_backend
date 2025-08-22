import os
import pandas as pd
from src.utils.customLogger import logger

def ensureDbFiles(targetFolder,fileSpecs):
    
    if not os.path.exists(targetFolder):
        os.makedirs(targetFolder)

    for fileName,columns in fileSpecs.items():
        filePath=os.path.join(targetFolder,fileName)
        if not os.path.exists(filePath):
            logger.info(f"Creating {filePath}...")
            df=pd.DataFrame(columns=columns)
            df.to_excel(filePath,index=False)
        else:
            logger.info(f"{filePath} already exists.")

