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
    LogPiece Input Model
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
    LogPiece Output Model
    """
    output_log: str = Field(
        description='All values logged.'
    )
    output_str: Optional[str] = Field(
        description='Output string logged.'
    )
    output_int: Optional[int] = Field(
        description='Output integer logged.'
    )
    output_float: Optional[float] = Field(
        description='Output float logged.'
    )
    output_bool: Optional[bool] = Field(
        description='Output boolean logged.'
    )
    output_enum: Optional[str] = Field(
        description='Output enum logged.'
    )
    output_date: date = Field(
        description='Output date logged.'
    )
    output_time: time = Field(
        description='Output time logged.',
    )
    output_datetime: datetime = Field(
        description='Output datetime logged.'
    )
    output_array: List[str] = Field(
        description='Output array logged.'
    )
    output_code: str = Field(
        description='Output code logged.',
        json_schema_extra={
            'widget': "codeeditor",
        }
    )
