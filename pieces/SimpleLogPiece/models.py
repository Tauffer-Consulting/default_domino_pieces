from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Example Operator
    """

    input_arg_1: str = Field(
        default='default',
        description='description'
    )


class OutputModel(BaseModel):
    """
    Example Operator
    """
    message: str = Field(
        default="",
        description="Output message to log"
    )
    output_arg_1: str = Field(
        default='default',
        description='description'
    )


class SecretsModel(BaseModel):
    """
    Example Operator Secrets
    """

    EXAMPLE_VAR: str = Field(
        description="Example secret var"
    )