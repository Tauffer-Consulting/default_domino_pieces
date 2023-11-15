from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import requests
import base64
import json


class HttpRequestPiece(BasePiece):
    def piece_function(self, input_data: InputModel):

        try:
            url = input_data.url
            method = input_data.method

            headers = {}
            if input_data.bearer_token:
                headers['Authorization'] = f'Bearer {input_data.bearer_token}'

            # Prepare the request body if applicable
            body_data = None
            if method in ["POST", "PUT"]:
                try:
                    body_data = json.loads(input_data.body_json_data)
                except json.JSONDecodeError:
                    raise Exception("Invalid JSON data in the request body.")

            # Send the HTTP request
            if method == "GET":
                response = requests.get(url, headers=headers)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=body_data)
            elif method == "PUT":
                response = requests.put(url, headers=headers, json=body_data)
            elif method == "DELETE":
                response = requests.delete(url, headers=headers)
            else:
                raise Exception(f"Unsupported HTTP method: {method}")

            # Check for HTTP errors
            response.raise_for_status()

        except requests.RequestException as e:
            raise Exception(f"HTTP request error: {e}")

        # convert content to base64
        base64_bytes_data = base64.b64encode(response.content).decode('utf-8')
        return OutputModel(base64_bytes_data=base64_bytes_data)
