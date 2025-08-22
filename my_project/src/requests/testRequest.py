from src.config.testReplyConfigManager import testReplyConfigurationManager
from src.modules.database.dbTestReply import databaseInitTestReplyHandler

class testRequestHandler:
    def __init__(self,data:dict):
        self.data=data
        self.config=testReplyConfigurationManager(data=self.data)
        self.dbConfig=self.config.databaseTestInitManager()
        db=databaseInitTestReplyHandler(self.dbConfig)
        self.success=db.dbInit()

    def returnConfig(self):
        if self.success:
            if self.data["testType"]=="testByDifficulty":
                configuration=self.config.testByDifficultyConfiguration()
                return configuration
            elif self.data["testType"]=="testByCompanies":
                configuration=self.config.testByCompaniesConfiguration()
                return configuration
            elif self.data["testType"]=="testbyGenAI":
                configuration=self.config.testByGenAIConfiguration()
                return configuration
        else:
            return None
        
    
            

    