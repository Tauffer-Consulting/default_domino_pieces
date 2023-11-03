from pydantic import BaseModel, Field



class InputModel(BaseModel):
    """
    GetDateTimePiece Input Model
    """
    api_url: str = Field(
        description='Input data to be converted. Can be a file path or data as string.'
    )


class OutputModel(BaseModel):
    """
    GetDateTimePiece Output Model
    """
    base64_bytes_data: str = Field(
        description='Output data as base64 encoded string.'
    )