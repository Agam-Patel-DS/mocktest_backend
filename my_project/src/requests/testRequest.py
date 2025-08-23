from src.config.testReplyConfigManager import testReplyConfigurationManager
from src.modules.database.dbTestReply import databaseInitTestReplyHandler, databaseTestDetailsTestReplyHandler

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
                dbConfig=self.config.databaseTestDetailsManager()
                db=databaseTestDetailsTestReplyHandler(dbConfig)
                db.dbTestDetailsInit()
                return configuration
            elif self.data["testType"]=="testByCompanies":
                configuration=self.config.testByCompaniesConfiguration()
                dbConfig=self.config.databaseTestDetailsManager()
                db=databaseTestDetailsTestReplyHandler(dbConfig)
                db.dbTestDetailsInit()
                return configuration
            elif self.data["testType"]=="testbyGenAI":
                configuration=self.config.testByGenAIConfiguration()
                dbConfig=self.config.databaseTestDetailsManager()
                db=databaseTestDetailsTestReplyHandler(dbConfig)
                db.dbTestDetailsInit()
                return configuration
        else:
            return None
        
    
            

    