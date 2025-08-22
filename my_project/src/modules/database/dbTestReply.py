import pandas as pd
from src.modules.database import ensureDbFiles
from src.utils import loadConfig
from src.entity.testReplyConfigs import databaseTestInitConfig
import os
from src.utils.customLogger import logger

class databaseInitTestReplyHandler:
    def __init__(self,config:databaseTestInitConfig):
        self.config=config
        self.fileConfig=loadConfig("config/dbconfig.yaml")
        logger.info("Ensuring DB exists...")
        ensureDbFiles(self.fileConfig.target,vars(self.fileConfig.filesAndColumns))

    def dbInit(self):
        filePath=self.fileConfig.userTestFilePath
        columns=self.fileConfig.testUserDetails
        values=[self.config.userId,self.config.testId, self.config.testType]
        newRow=pd.DataFrame([values], columns=columns)
        if os.path.exists(filePath):
            df=pd.read_excel(filePath)
            for col in columns:
                if col not in df.columns:
                    df[col]=None
            
            if "testId" in df.columns:
                newVal=newRow.iloc[0]["testId"]
                if newVal in df["testId"].values:
                    logger.info(f"Duplicate testId for {values} found")
                    return False
            df=pd.concat([df,newRow],ignore_index=True)
        else:
            df=newRow

        df.to_excel(filePath,index=False)
        logger.info(f"User-Test Details {values} Added to table {filePath}")
        return True

