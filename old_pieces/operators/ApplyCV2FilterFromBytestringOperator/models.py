from pydantic import BaseModel, Field
from enum import Enum


class EffectType(str, Enum):
    random = "random"
    grayscale = "grayscale"
    bright = "bright"
    dark = "dark"
    sharp = "sharp"
    sepia = "sepia"
    pencil = "pencil"
    pencil_color = "pencil_color"
    hdr = "hdr"
    invert = "invert"
    summer = "summer"
    winter = "winter"


class InputModel(BaseModel):
    """
    Apply effect to image
    """

    bytestring_image: str = Field(
        description="Image as a bytestring",
    )
    effect: EffectType = Field(
        default='random',
        description='Effect to be applied'
    )

class OutputModel(BaseModel):
    """
    Apply effect to image
    """

    bytestring_image: str = Field(
        description="Output image as a bytestring",
    )

class SecretsModel(BaseModel):
    """
    Secrets for Apply effect to image
    """

    pass