from domino.base_piece import BasePiece
from pathlib import Path
from io import StringIO
import pandas as pd
from .models import InputModel, OutputModel
import requests
import base64


class ApiFetchPiece(BasePiece):
    def piece_function(self, input_data: InputModel):

        api_url = input_data.api_url

        response = requests.get(api_url)

        # convert content to base64
        base64_bytes_data = base64.b64encode(response.content).decode('utf-8')
        return OutputModel(base64_bytes_data=base64_bytes_data)
