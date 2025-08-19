from dataclasses import dataclass
from src.utils import readData

@dataclass
class testByDifficultyConfig:
    difficultyLevel: list
    dataStructure: list
    numberOfQuestions: int
    excelPath: str
    seed:int