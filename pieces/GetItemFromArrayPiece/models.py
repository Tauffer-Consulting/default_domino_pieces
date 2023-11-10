from pydantic import BaseModel, Field
from typing import Union
from datetime import date as dt_date, datetime as dt_datetime, time as dt_time
from enum import Enum


class IndexType(str, Enum):
    first = 'first'
    last = 'last'
    random = 'random'
    another = 'another'


class InputModel(BaseModel):
    """
    GetItemFromArrayPiece Input Model
    """
    input_array: list = Field(
        description='Input array to get item from.',
        json_schema_extra={
            "from_upstream": "always"
        }
    )
    index: IndexType = Field(
        default=IndexType.first,
        description='Index of item to get from input array.'
    )
    another_index: int = Field(
        default=1,
        ge=1,
        description='Index number of item to get from input array.'
    )


class OutputModel(BaseModel):
    """
    GetItemFromArrayPiece Output Model
    """
    output_value: Union[str, list, int, float, bool, dict, dt_date, dt_time, dt_datetime] = Field(
        description='Item from input array at specified index.'
    )
