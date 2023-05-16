from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    SimpleLogPiece Input Model
    """

    input_msg: str = Field(
        default="",
        description='Input to be logged'
    )


class OutputModel(BaseModel):
    """
    SimpleLogPiece Output Model
    """
    message: str = Field(
        default="",
        description="Output message to log"
    )
    output_msg: str = Field(
        description='Value that was logged'
    )