from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    CustomPythonPiece Input Model
    """
    input_args: list = Field(
        default=[],
        description='Input args.'
    )
    script: str = Field(
        default="""
def main(input_args):
    return input_args
""",
        description='Python script.',
        widget="codeeditor"
    )
    output_args: list = Field(
        default=[],
        description='Output args.'
    )


class OutputModel(BaseModel):
    """
    CustomPythonPiece Output Model
    """
    error: str = Field(
        default=None,
        description='Error message.'
    )