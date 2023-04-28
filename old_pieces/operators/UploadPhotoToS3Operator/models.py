from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Upload photo from mounted volume to S3 folder
    """

    s3_bucket_name: str = Field(
        default='bucket-name',
        description='Name of the bucket'
    )
    s3_folder_name: str = Field(
        default='edited',
        description='Folder path within the bucket'
    )
    input_file_path: str = Field(
        description='The file path to be uploaded'
    )


class OutputModel(BaseModel):
    """
    Upload photo from mounted volume to S3 folder
    """
    message: str = Field(
        default="",
        description="Output message to log"
    )
    file_url: str = Field(
        description="Url for the uploaded file"
    )