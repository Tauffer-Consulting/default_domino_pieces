from flowui.base_operator import BaseOperator
from flowui.client.s3_client import S3Client
from .models import InputModel, OutputModel

from pathlib import Path
import botocore


class UploadPhotoToS3Operator(BaseOperator):
    
    def operator_function(self, input_model: InputModel):
        s3_client = S3Client(bucket_name=input_model.s3_bucket_name)

        try:
            target_s3_path = f"{input_model.s3_folder_name}/{Path(input_model.input_file_path).name}"
            s3_client.upload_file_to_s3(
                object_key=target_s3_path, 
                file_path=input_model.input_file_path
            )
            file_url = ""  # TODO
        except botocore.exceptions.ClientError as e:
            raise e

        return OutputModel(
            message="Photo successfully uploaded to S3!",
            file_url=file_url
        )