from domino.testing import piece_dry_run
from datetime import datetime


def test_stringpiece_int():
    input_data = dict(
        input_value=10
    )
    piece_output = piece_dry_run(
        piece_name="ToStringPiece",
        input_data=input_data
    )
    assert str(10) == piece_output.output_value


def test_stringpiece_float():
    input_data = dict(
        input_value=10.5
    )
    piece_output = piece_dry_run(
        piece_name="ToStringPiece",
        input_data=input_data
    )
    assert str(10.5) == piece_output.output_value


def test_stringpiece_bool():
    input_data = dict(
        input_value=True
    )
    piece_output = piece_dry_run(
        piece_name="ToStringPiece",
        input_data=input_data
    )
    assert str(True) == piece_output.output_value


def test_stringpiece_list():
    input_data = dict(
        input_value=[1, 2, 3]
    )
    piece_output = piece_dry_run(
        piece_name="ToStringPiece",
        input_data=input_data
    )
    assert str([1, 2, 3]) == piece_output.output_value


def test_stringpiece_dict():
    input_data = dict(
        input_value={"a": 1, "b": 2}
    )
    piece_output = piece_dry_run(
        piece_name="ToStringPiece",
        input_data=input_data
    )
    assert str({"a": 1, "b": 2}) == piece_output.output_value


def test_stringpiece_datetime():
    now = datetime.now()
    input_data = dict(
        input_value=now,
    )
    piece_output = piece_dry_run(
        piece_name="ToStringPiece",
        input_data=input_data
    )
    assert str(now) == piece_output.output_value


def test_stringpiece_date():
    now = datetime.now().date()
    input_data = dict(
        input_value=now,
    )
    piece_output = piece_dry_run(
        piece_name="ToStringPiece",
        input_data=input_data
    )
    assert str(now) == piece_output.output_value


def test_stringpiece_time():
    now = datetime.now().time()
    input_data = dict(
        input_value=now,
    )
    piece_output = piece_dry_run(
        piece_name="ToStringPiece",
        input_data=input_data
    )
    assert str(now) == piece_output.output_value
