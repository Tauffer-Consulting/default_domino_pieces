from pydantic import BaseModel, Field
from enum import Enum

class DatasetName(str, Enum):
    iris = "iris"
    diabetes = "diabetes"
    digits = "digits"
    wine = "wine"
    breast_cancer = "breast_cancer"
    linnerrud = "linnerrud"

class InputModel(BaseModel):
    dataset: DatasetName = Field(default='iris', title='Dataset name')

class OutputModel(BaseModel):
    data: list[dict]
