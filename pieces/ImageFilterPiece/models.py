from pydantic import BaseModel, Field
from enum import Enum


class OutputTypeType(str, Enum):
    """
    Output type for the result text
    """
    file = "file"
    base64_string = "base64_string"
    both = "both"


class InputModel(BaseModel):
    input_image: str = Field(
        description='Input image. It should be either a path to a file, or a base64 encoded string.',
        json_schema_extra={
            "from_upstream": "always"
        }
    )
    sepia: bool = Field(
        default=False,
        description='Apply sepia effect.',
    )
    black_and_white: bool = Field(
        default=False,
        description='Apply black and white effect.',
    )
    brightness: bool = Field(
        default=False,
        description='Apply brightness effect.',
    )
    darkness: bool = Field(
        default=False,
        description='Apply darkness effect.',
    )
    contrast: bool = Field(
        default=False,
        description='Apply contrast effect.',
    )
    red: bool = Field(
        default=False,
        description='Apply red effect.',
    )
    green: bool = Field(
        default=False,
        description='Apply green effect.',
    )
    blue: bool = Field(
        default=False,
        description='Apply blue effect.',
    )
    cool: bool = Field(
        default=False,
        description='Apply cool effect.',
    )
    warm: bool = Field(
        default=False,
        description='Apply warm effect.',
    )
    output_type: OutputTypeType = Field(
        default=OutputTypeType.both,
        description='Format of the output image. Options are: `file`, `base64_string`, `both`.',
    )


class OutputModel(BaseModel):
    image_base64_string: str = Field(
        default='',
        description='Base64 encoded string of the output image.',
    )
    image_file_path: str = Field(
        default='',
        description='Path to the output image file.',
    )
