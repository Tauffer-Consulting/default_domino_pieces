from pydantic import BaseModel, Field
from enum import Enum


class DistributionType(str, Enum):
    gaussian = "gaussian"
    poisson = "poisson"


class InputModel(BaseModel):
    distribution_name: DistributionType = Field(
        description="Name of the distribution to sample from"
    )
    distribution_mean: float = Field(
        description="Distribution mean"
    )
    distribution_sd: float = Field(
        default=1.,
        gt=0.,
        description="Distribution standard deviation"
    )


class OutputModel(BaseModel):
    message: str = Field(
        description="Output message to log"
    )
    sample_result: str = Field(
        description="The result of this Piece's processing"
    )


class SecretsModel(BaseModel):
    EXAMPLE_OPERATOR_SECRET_1: str = Field(
        description="A secret necessary to run this Piece"
    )