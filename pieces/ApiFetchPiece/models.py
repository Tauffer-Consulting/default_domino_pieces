from pydantic import BaseModel, Field



class InputModel(BaseModel):
    api_url: str = Field(
        description='Input data to be converted. Can be a file path or data as string.'
    )


class OutputModel(BaseModel):
    base64_bytes_data: str = Field(
        description='Output data as base64 encoded string.'
    )