from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Example Operator
    """

    airbnb_location_id: str = Field(
        default='ChIJN3P2zJlG0i0RACx9yvsLAwQ',
        description='Airbnb location id to search'
    )
    currency: str = Field(
        default='USD',
        description='Currency to use in price'
    )
    adults: int = Field(
        default=1,
        description='Number of adults'
    )




class OutputModel(BaseModel):
    """
    Example Operator
    """
    data: list = Field(
        description="Output list with airbnb data"
    )
    message: str = Field(description="Message to log")


class SecretsModel(BaseModel):
    """
    Example Operator Secrets
    """

    API_KEY: str = Field(
        description="API key"
    )