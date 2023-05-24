from pydantic import BaseModel, Field
from enum import Enum
from typing import List


class InputEnum(str, Enum):
    option1 = "option1"
    option2 = "option2"
    option3 = "option3"


class InputModel(BaseModel):
    """
    SimpleLogPiece Input Model
    """
    input_str: str = Field(
        default="default value",
        description='Input string to be logged.'
    )
    input_int: int = Field(
        default=10,
        description='Input integer to be logged.'
    )
    input_float: float = Field(
        default=10.5,
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
    input_date: str = Field(
        default="2023-01-01",
        description='Input date to be logged.',
        widget="date"
    )
    input_time: str = Field(
        default="16:20",
        description='Input time to be logged.',
        widget="time"
    )
    input_datetime: str = Field(
        default="2023-01-01T16:20",
        description='Input datetime to be logged.',
        widget="datetime"
    )
    input_array: List[str] = Field(
        default=["default_1", "default_2", "default_3"],
        description='Input array to be logged.'
    )


class OutputModel(BaseModel):
    """
    SimpleLogPiece Output Model
    """
    message: str = Field(
        default="",
        description="Output message to log."
    )
    output_msg: str = Field(
        description='Value that was logged.'
    )