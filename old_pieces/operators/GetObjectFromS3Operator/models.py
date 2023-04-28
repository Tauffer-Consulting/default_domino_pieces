from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Get object from S3 input model
    """

    bucket_name: str = Field(
        default='bucket-name',
        description='this is the name of the bucket'
    )

    path: str = Field(
        default='path/to/object',
        description='this is the path to the object'
    )


class OutputModel(BaseModel):
    """
    Get photo from S3 output model
    """
    bytes_object: str = Field(
        description="Output bytestring object"
    )

class SecretsModel(BaseModel):
    """
    Example Operator Secrets
    """
    AWS_ACCESS_KEY_ID: str = Field(
        description="AWS Access Key ID"
    )
    AWS_SECRET_ACCESS_KEY: str = Field(
        description="AWS Secret Access Key"
    )