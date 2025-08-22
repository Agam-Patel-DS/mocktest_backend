from dataclasses import dataclass


@dataclass
class databaseSolutionDetailsConfig:
    userId:str
    testId:str
    solutions:dict
    timeTaken:int

@dataclass
class databaseScoreConfig:
    userId:str
    testId:str
    score:int
    result:dict
