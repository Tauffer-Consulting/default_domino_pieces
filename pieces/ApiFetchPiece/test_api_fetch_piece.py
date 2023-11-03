from domino.testing import piece_dry_run
import base64
import json


def test_api_fetch_piece():
    api_url = 'https://jsonplaceholder.typicode.com/posts'

    input_data = {
        'api_url': api_url
    }

    piece_output = piece_dry_run(
        piece_name="ApiFetchPiece",
        input_data=input_data
    )
    output_data = base64.decodebytes(piece_output['base64_bytes_data'].encode('utf-8'))
    output_data = json.loads(output_data)
    
    assert isinstance(output_data, list)
    
