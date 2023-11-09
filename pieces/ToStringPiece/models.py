from pydantic import BaseModel, Field
from typing import Union
from datetime import date as dt_date, datetime as dt_datetime, time as dt_time


class InputModel(BaseModel):
    """
    ToStringPiece Input Model
    """
    input_value: Union[str, list, int, float, bool, dict, dt_date, dt_time, dt_datetime] = Field(
        description='Input value to be turned into string.',
        json_schema_extra={
            "from_upstream": "always"
        }
    )


class OutputModel(BaseModel):
    """
    ToStringPiece Output Model
    """
    output_value: str = Field(
        description='Input value as a string.'
    )
