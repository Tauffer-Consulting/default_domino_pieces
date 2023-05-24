from pydantic import BaseModel, Field, Extra
from typing import List
from enum import Enum


class OutputArgsType(str, Enum):
    """
    OutputArgsType Enum
    """
    string = 'string'
    integer = 'integer'
    float = 'float'
    boolean = 'boolean'
    array = 'array'
    

class OutputArgsModel(BaseModel):
    name: str = Field(
        default=None,
        description='Name of the output arg.',
        from_upstream="never"
    )
    type: OutputArgsType = Field(
        default=OutputArgsType.string,
        description='Type of the output arg.',
        from_upstream="never"
    )


class InputModel(BaseModel):
    """
    CustomPythonPiece Input Model
    """
    input_args: list = Field(
        default=[],
        description='Input args.',
        from_upstream="always"
    )
    script: str = Field(
        default="""
def main(input_args):
    return input_args
""",
        description='Python script.',
        widget="codeeditor",
        from_upstream="never"
    )
    output_args: List[OutputArgsModel] = Field(
        default=[],
        description='Output args.',
        from_upstream="never"
    )


class OutputModel(BaseModel, extra=Extra.allow):
    """
    CustomPythonPiece Output Model
    """
    # ref: https://stackoverflow.com/a/75381426/11483674
    pass