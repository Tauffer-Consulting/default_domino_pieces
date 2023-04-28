from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Download random file from Github
    """

    repository_name: str = Field(
        description='The name of the target repository'
    )
    branch: str = Field(
        default="main",
        description='The branch to be used'
    )
    folder_path: str = Field(
        description='The folder path within the repository'
    )


class OutputModel(BaseModel):
    """
    Download random file from Github
    """

    message: str = Field(
        default="",
        description="Output message to log"
    )
    output_file_path: str = Field(
        description='The path to the downloaded file'
    )


class SecretsModel(BaseModel):
    """
    Download random file from Github
    """

    GITHUB_ACCESS_TOKEN: str = Field(
        description="Github access token"
    )