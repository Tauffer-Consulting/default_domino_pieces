from flowui.base_operator import BaseOperator
from flowui.client.s3_client import S3Client
from .models import InputModel, OutputModel

import random
import base64
import botocore


class LoadPhotoFromS3Operator(BaseOperator):
    
    def operator_function(self, input_model: InputModel):
        s3_client = S3Client(bucket_name=input_model.bucket_name)

        try:
            all_objs = s3_client.list_objects_from_bucket()
            random_obj = all_objs[random.randint(0, len(all_objs) - 1)]

            if input_model.save_as_file:
                # Save photo to mounted volume
                output_file_path = str(self.results_path / random_obj.key)
                s3_client.download_file_from_s3_folder(
                    object_key=random_obj.key, 
                    file_path=output_file_path
                )
                message = f"Image successfully downloaded and saved to: {output_file_path}"
                image_data_string = None
            else:
                # Send photo to XCOM
                file_bytes = s3_client.download_file_from_s3_folder_as_bytes(object_key=random_obj.key)
                image_data_bytes_b64 = base64.b64encode(file_bytes.read())
                image_data_string = image_data_bytes_b64.decode('utf-8')
                message = "Image successfully downloaded and sent through XCOM."
                output_file_path = None
        except botocore.exceptions.ClientError as e:
            raise e

        return OutputModel(
            message=message,
            output_file_path=output_file_path,
            image_data=image_data_string
        )