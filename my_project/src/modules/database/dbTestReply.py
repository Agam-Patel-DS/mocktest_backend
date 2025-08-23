import pandas as pd
from src.modules.database import ensureDbFiles
from src.utils import loadConfig
from src.entity.testReplyConfigs import databaseTestInitConfig, databaseTestDetailsConfig, databaseQuestionDetailsConfig
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
        values=[self.config.userId,self.config.testId, self.config.testType, self.config.timeStamp]
        newRow=pd.DataFrame([values], columns=columns)
        if os.path.exists(filePath):
            df=pd.read_excel(filePath)
            for col in columns:
                if col not in df.columns:
                    df[col]=None
            
            if {"userId","testId"}.issubset(df.columns):
                newUser=newRow.iloc[0]["userId"]
                newTest=newRow.iloc[0]["testId"]
                if((df["userId"]==newUser)&(df["testId"]==newTest)).any():
                    logger.info(f"Duplicate entry to {values[0]} having testId {values[1]} found. Not Registered.")
                    return False
                
            df=pd.concat([df,newRow],ignore_index=True)
        else:
            df=newRow

        df.to_excel(filePath,index=False)
        logger.info(f"User-Test Details {values} Added to table {filePath}")
        return True

class databaseTestDetailsTestReplyHandler:
    def __init__(self,config:databaseTestDetailsConfig):
        self.config=config
        self.fileConfig=loadConfig("config/dbconfig.yaml")
        logger.info("Ensuring DB exists...")
        ensureDbFiles(self.fileConfig.target,vars(self.fileConfig.filesAndColumns))

    def dbTestDetailsInit(self):
        filePath=self.fileConfig.testDetailsFilePath
        columns=self.fileConfig.testDetails
        values=[self.config.userId,self.config.testId, self.config.numberOfQuestions, self.config.difficultyLevel,self.config.companies, self.config.dataStructures, self.config.timeLimit]
        newRow=pd.DataFrame([values], columns=columns)
        if os.path.exists(filePath):
            df=pd.read_excel(filePath)
            for col in columns:
                if col not in df.columns:
                    df[col]=None
            
            if {"userId","testId"}.issubset(df.columns):
                newUser=newRow.iloc[0]["userId"]
                newTest=newRow.iloc[0]["testId"]
                if((df["userId"]==newUser)&(df["testId"]==newTest)).any():
                    logger.info(f"Duplicate entry to {values[0]} having testId {values[1]} found. Not Registered.")
                    return False
                
            df=pd.concat([df,newRow],ignore_index=True)
        else:
            df=newRow

        df.to_excel(filePath,index=False)
        logger.info(f"Test Details {values} Added to table {filePath}")
        return True


class databaseQuestionDetailsTestReplyHandler:
    def __init__(self,config:databaseQuestionDetailsConfig):
        self.config=config
        self.fileConfig=loadConfig("config/dbconfig.yaml")
        logger.info("Ensuring DB exists...")
        ensureDbFiles(self.fileConfig.target,vars(self.fileConfig.filesAndColumns))

    def dbQuestionDetailsInit(self):
        filePath=self.fileConfig.questionDetailsFilePath
        columns=self.fileConfig.questionDetails
        values=[self.config.userId,self.config.testId, self.config.questionIds]
        newRow=pd.DataFrame([values], columns=columns)
        if os.path.exists(filePath):
            df=pd.read_excel(filePath)
            for col in columns:
                if col not in df.columns:
                    df[col]=None
            
            if {"userId","testId"}.issubset(df.columns):
                newUser=newRow.iloc[0]["userId"]
                newTest=newRow.iloc[0]["testId"]
                if((df["userId"]==newUser)&(df["testId"]==newTest)).any():
                    logger.info(f"Duplicate entry to {values[0]} having testId {values[1]} found. Not Registered.")
                    return False
                
            df=pd.concat([df,newRow],ignore_index=True)
        else:
            df=newRow

        df.to_excel(filePath,index=False)
        logger.info(f"Test Details {values} Added to table {filePath}")
        return True