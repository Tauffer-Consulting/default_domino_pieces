from pydantic import BaseModel, Field
from enum import Enum

class InputEnum(str, Enum):
    option1 = "option1"
    option2 = "option2"
    option3 = "option3"

class InputModel(BaseModel):
    """
    SimpleLogPiece Input Model
    """
    input_str: str = Field(
        default="",
        description='Input string to be logged.'
    )
    input_int: int = Field(
        default=0,
        description='Input integer to be logged.'
    )
    input_float: float = Field(
        default=0.0,
        description='Input float to be logged.'
    )
    input_bool: bool = Field(
        default=False,
        description='Input boolean to be logged.'
    )
    input_enum: InputEnum = Field(
        default=InputEnum.option1,
        description='Input enum to be logged.'
    )
    input_list: list = Field(
        default=[],
        description='Input list to be logged.'
    )


class OutputModel(BaseModel):
    """
    SimpleLogPiece Output Model
    """
    message: str = Field(
        default="",
        description="Output message to log"
    )
    output_msg: str = Field(
        description='Value that was logged'
    )