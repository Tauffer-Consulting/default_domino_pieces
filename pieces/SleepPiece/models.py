from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Sleep Piece Input Model
    """

    sleep_time: float = Field(
        default=1,
        required=True,
        description="Number of seconds to sleep"
    )


class OutputModel(BaseModel):
    """
    Sleep Piece Output Model
    """
    message: str = Field(
        default="",
        description="Sleep piece executed"
    )