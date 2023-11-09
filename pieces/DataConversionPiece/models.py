from pydantic import BaseModel, Field
from enum import Enum


class DataFormatOption(str, Enum):
    csv = 'csv'
    json = 'json'


class InputModel(BaseModel):
    input_data: str = Field(
        description='Input data to be converted. Can be a file path or data as string.'

    )
    input_data_format: DataFormatOption = Field(
        default=DataFormatOption.csv,
        description='Input data format to be converted.'
    )
    output_data_format: DataFormatOption = Field(
        default=DataFormatOption.json,
        description='Output data format.'
    )


class OutputModel(BaseModel):
    output_file_path: str = Field(
        description='Path to the converted file.'
    )
