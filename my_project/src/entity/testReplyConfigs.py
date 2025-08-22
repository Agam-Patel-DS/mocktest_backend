from dataclasses import dataclass

@dataclass
class testByDifficultyConfig:
    difficultyLevel: list
    dataStructure: list
    numberOfQuestions: int
    excelPath: str
    seed:int

@dataclass
class testByCompaniesConfig:
    companies: list
    difficultyLevel: list
    numberOfQuestions: int
    excelPath: str
    seed: int

@dataclass
class testByGenAIConfig:
    numberOfQuestions: int
    difficultyLevel: int
    dataStructure: list