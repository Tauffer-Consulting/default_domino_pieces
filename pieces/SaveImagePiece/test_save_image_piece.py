from domino.testing import piece_dry_run
import base64
import json
import requests



def test_api_fetch_piece():
    picsum_url = "https://picsum.photos/400/400"
    response = requests.get(picsum_url)

    base64_encoded_content = base64.b64encode(response.content).decode('utf-8')

    input_data = {
        'base64_data': base64_encoded_content
    }

    piece_output = piece_dry_run(
        piece_name="SaveImagePiece",
        input_data=input_data
    )

    
    assert piece_output['output_image_path'].endswith('output_image.png')
    
