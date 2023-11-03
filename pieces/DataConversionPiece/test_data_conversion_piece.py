from domino.testing import piece_dry_run
import pandas as pd


def test_data_conversion_piece():
    df = pd.DataFrame({'date': ['2021-01-01 00:00:00', '2021-01-01 00:00:00', '2021-01-01 00:00:00']})
    input_data = {'input_data': df.to_csv(), 'input_data_format': 'csv', 'output_data_format': 'json'}

    piece_output = piece_dry_run(
        piece_name="DataConversionPiece",
        input_data=input_data
    )

    assert piece_output['output_file_path'].endswith('output.json')
    
