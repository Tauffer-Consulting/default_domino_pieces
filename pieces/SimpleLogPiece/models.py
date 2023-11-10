from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional
from datetime import datetime, time, date


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
    input_date: date = Field(
        default="2023-01-01",
        description='Input date to be logged.'
    )
    input_time: time = Field(
        default="16:20:00",
        description='Input time to be logged.',
    )
    input_datetime: datetime = Field(
        default="2023-01-01T16:20:00",
        description='Input datetime to be logged.'
    )
    input_array: List[str] = Field(
        default=["default_1", "default_2", "default_3"],
        description='Input array to be logged.'
    )
    input_code: str = Field(
        default="print('Hello world!')",
        description='Input code to be logged.',
        json_schema_extra={
            'widget': "codeeditor",
        }
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

    # Outputs types
    output_str: Optional[str] = Field(
        description='Output string to be logged.'
    )
    output_int: Optional[int] = Field(
        description='Output integer to be logged.'
    )
    output_float: Optional[float] = Field(
        description='Output float to be logged.'
    )
    output_bool: Optional[bool] = Field(
        description='Output boolean to be logged.'
    )
    output_date: date = Field(
        description='Output date to be logged.'
    )
    output_time: time = Field(
        description='Output time to be logged.',
    )
    output_datetime: datetime = Field(
        description='Output datetime to be logged.'
    )
    output_array: List[str] = Field(
        description='Output array to be logged.'
    )
    output_code: str = Field(
        description='Input code to be logged.',
        json_schema_extra={
            'widget': "codeeditor",
        }
    )
