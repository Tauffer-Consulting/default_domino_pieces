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
        default="""# Do not modify the function definition line 
def custom_function(input_args: list):
    # Write your code here
    print(input_args)

    # Return the output of the function as an object,
    # Matching the Output Args defined in the Form below
    return {
        "out_arg_1": "this is a string", 
        "out_arg_2": 420
    }
""",
        description='Python script.',
        widget="codeeditor",
        from_upstream="never"
    )
    output_args: List[OutputArgsModel] = Field(
        default=[
            OutputArgsModel(name="output_arg_1", type=OutputArgsType.string),
            OutputArgsModel(name="output_arg_2", type=OutputArgsType.integer),
        ],
        description='Output args.',
        from_upstream="never"
    )


class OutputModel(BaseModel, extra=Extra.allow):
    """
    CustomPythonPiece Output Model
    """
    # ref: https://stackoverflow.com/a/75381426/11483674
    pass