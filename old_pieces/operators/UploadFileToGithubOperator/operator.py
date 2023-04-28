from flowui.base_operator import BaseOperator
from flowui.client.github_rest_client import GithubRestClient
from .models import InputModel, OutputModel

from pathlib import Path


class UploadFileToGithubOperator(BaseOperator):
    
    def operator_function(self, input_model: InputModel):
        github_client = GithubRestClient()

        with open(input_model.input_file_path, "rb") as f:
            encoded_string = f.read()

        file_target = f"edited/{Path(input_model.input_file_path).name}"
        github_client.create_file(
            repo_name=input_model.repository_name, 
            file_path=file_target, 
            content=encoded_string
        )
        file_url = f"https://github.com/{input_model.repository_name}/raw/{input_model.branch}/{file_target}"
        
        return OutputModel(
            message="File successfully uploaded to Github!",
            file_url=file_url
        )