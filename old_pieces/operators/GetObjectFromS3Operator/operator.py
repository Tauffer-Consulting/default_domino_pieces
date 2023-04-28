from flowui.base_operator import BaseOperator
import boto3
from .models import InputModel, OutputModel
from botocore.exceptions import ClientError


class GetObjectFromS3Operator(BaseOperator):
    def operator_function(self, input_model: InputModel):
        """
        Get object from S3 and return it as a bytestring
        """
        self.logger.info('Getting object from S3')
        s3_client = boto3.client("s3", aws_access_key_id=self.secrets.AWS_ACCESS_KEY_ID, aws_secret_access_key=self.secrets.AWS_SECRET_ACCESS_KEY)
    
        bucket = input_model.bucket_name
        path = input_model.path
        try:
            resp = s3_client.get_object(Bucket=bucket, Key=path)
        except ClientError as e:
            self.logger.error(e)
            raise e
        self.logger.info('Object retrieved')

        encoding = 'ISO-8859-1' # TODO change to model input
        bytes_object = resp.get("Body").read().decode(encoding)

        return OutputModel(
            bytes_object=bytes_object
        )