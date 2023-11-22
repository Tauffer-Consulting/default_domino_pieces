from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional

class DatasetName(str, Enum):
    iris = "iris"
    diabetes = "diabetes"
    digits = "digits"
    wine = "wine"
    breast_cancer = "breast_cancer"
    linnerrud = "linnerrud"

class OutputType(str, Enum):
    file = "file"
    object = "object"

class InputModel(BaseModel):
    dataset: DatasetName = Field(default='iris', title='Dataset name')
    output_type: OutputType = Field(default='object', title='Output type', description='Whether to return a file or an object. Use files for large data')

class OutputModel(BaseModel):
    data: Optional[List[dict]]
    file_path: Optional[str]
