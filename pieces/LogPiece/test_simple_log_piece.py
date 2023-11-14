from domino.testing import piece_dry_run


def test_log_piece():
    input_data = dict(
        input_str='test string',
        input_int=10,
        input_float=10.5,
        input_bool=False,
        input_enum="option1",
        input_date="2023-01-01",
        input_time="16:20:00",
        input_datetime="2023-01-01T16:20:00",
        input_array=["default_1", "default_2", "default_3"],
        input_code="print('Hello world!')"
    )

    piece_output = piece_dry_run(
        repository_folder_path=".",
        piece_name="LogPiece",
        input_data=input_data
    )

    mock_output = dict(
        output_str=input_data.get("input_str"),
        output_int=input_data.get("input_int"),
        output_float=input_data.get("input_float"),
        output_bool=input_data.get("input_bool"),
        output_enum=input_data.get("input_enum"),
        output_array=input_data.get("input_array"),
        output_date=input_data.get("input_date"),
        output_time=input_data.get("input_time"),
        output_datetime=input_data.get("input_datetime"),
        output_code=input_data.get("input_code")
    )

    for key, value in piece_output.items():
        if key in ['output_log']:
            assert isinstance(value, str)
            continue
        assert value == mock_output[key]
