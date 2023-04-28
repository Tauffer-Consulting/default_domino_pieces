from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Upload file to Github
    """

    repository_name: str = Field(
        description='The name of the target repository'
    )
    branch: str = Field(
        default="main",
        description='The branch to be used'
    )
    input_file_path: str = Field(
        description='The file path to be uploaded'
    )


class OutputModel(BaseModel):
    """
    Upload file to Github
    """
    message: str = Field(
        default="",
        description="Output message to log"
    )
    file_url: str = Field(
        description="Url for the uploaded file"
    )