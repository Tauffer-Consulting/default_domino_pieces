from pydantic import BaseModel, Field
from typing import Optional


class InputModel(BaseModel):
    data_path: str = Field(
        title='CSV file path',
        description='Path to the CSV file to be profiled',
        json_schema_extra={
            "from_upstream": "always"
        }
    )
    report_tile: Optional[str] = Field(title='Report title', description='Title of the report', default='Profiling Report')

class OutputModel(BaseModel):
    profile_file_path: str = Field(title='Output file path', description='Path to the output file.')
