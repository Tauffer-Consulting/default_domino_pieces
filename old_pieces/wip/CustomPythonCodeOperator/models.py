from pydantic import BaseModel, Field
from typing import List, Union
from enum import Enum


class OutputArgType(str, Enum):
    int = 'int'
    float = 'float'
    str = 'str'
    bool = 'bool'


class InputKwargsModel(BaseModel):
    key: str = Field(
        description="The key of the argument."
    )
    value: Union[int, float, str, bool] = Field(
        description="The value of the argument."
    )


class OutputKwargsModel(BaseModel):
    key: str = Field(
        description="The key of the argument."
    )
    arg_type: OutputArgType = Field(
        default=OutputArgType.str,
        description="The type of the argument."
    )


class InputModel(BaseModel):
    """
    Input data for CustomPythonCodeOperator
    """
    input_kwargs: List[InputKwargsModel] = Field(
        description='The input arguments to pass to the function.'
    )
    output_kwargs: List[OutputKwargsModel] = Field(
        description='The output arguments from the function.'
    )
    code: str = Field(
        description='The code to run.'
    )


class OutputModel(BaseModel):
    """
    Output data for CustomPythonCodeOperator
    """
    message: str = Field(
        description='The message to return.',
        default=''
    )
    output_kwargs: List[OutputKwargsModel] = Field(
        description='The output arguments from the function.'
    )