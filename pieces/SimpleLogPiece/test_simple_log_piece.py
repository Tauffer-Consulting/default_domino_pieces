from domino.testing import piece_dry_run
from datetime import datetime

def test_simple_log_piece():
    input_data = dict(
        input_str='test string',
        input_int=10,
        input_float=10.5,
        input_bool=False,
        input_enum="option1",
        input_date="2023-01-01",
        input_time="16:20",
        input_datetime="2023-01-01T16:20",
        input_array=["default_1", "default_2", "default_3"],
        input_code="print('Hello world!')"
    )

    piece_output = piece_dry_run(
        repository_folder_path=".",
        piece_name="SimpleLogPiece",
        input_data=input_data
    )

    mock_output = dict(
        message="Task successfully completed!",
        output_msg='test',
        output_str=input_data.get("input_str"),
        output_int=input_data.get("input_int"),
        output_float=input_data.get("input_float"),
        output_bool=input_data.get("input_bool"),
        output_array=input_data.get("input_array"),
        output_date=datetime.strptime(input_data.get("input_date"), '%Y-%m-%d').date(),
        output_time=datetime.strptime(input_data.get("input_time"), "%H:%M").time(),
        output_datetime=datetime.strptime(input_data.get("input_datetime"), "%Y-%m-%dT%H:%M").replace(tzinfo=None),
        output_code=input_data.get("input_code")
    )

    for key, value in piece_output.dict().items():
        if key in ['message', 'output_msg']:
            continue
        assert value == mock_output[key]