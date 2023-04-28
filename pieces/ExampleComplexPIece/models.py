from pydantic import BaseModel, Field
from enum import Enum


class InputModel(BaseModel):
    arg1: str = Field(
        description="Distribution mean"
    )


class OutputModel(BaseModel):
    message: str = Field(
        description="Output message to log"
    )
    result: str = Field(
        description="The result of this Piece's processing"
    )


class SecretsModel(BaseModel):
    EXAMPLE_OPERATOR_SECRET_2: str = Field(
        description="A secret necessary to run this Piece"
    )