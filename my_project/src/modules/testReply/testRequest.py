from src.modules.testReply.testReplyConfigManager import testReplyConfigurationManager


class testRequestHandler:
    def __init__(self,data:dict):
        self.data=data
        self.config=testReplyConfigurationManager(data=self.data)

    def returnConfig(self):
        if self.data["testType"]=="testByDifficulty":
            configuration=self.config.testByDifficultyConfiguration()
            return configuration
            

    