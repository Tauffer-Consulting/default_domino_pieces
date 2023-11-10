from domino.testing import piece_dry_run


def test_getitemfromarray_first():
    input_data = dict(
        input_array=[1, 2, 3, 4, 5],
        index="first"
    )
    piece_output = piece_dry_run(
        piece_name="GetItemFromArrayPiece",
        input_data=input_data
    )
    assert 1 == piece_output.get("output_value", None)


def test_getitemfromarray_last():
    input_data = dict(
        input_array=[1, 2, 3, 4, 5],
        index="last"
    )
    piece_output = piece_dry_run(
        piece_name="GetItemFromArrayPiece",
        input_data=input_data
    )
    assert 5 == piece_output.get("output_value", None)


def test_getitemfromarray_random():
    input_data = dict(
        input_array=[1, 2, 3, 4, 5],
        index="random"
    )
    piece_output = piece_dry_run(
        piece_name="GetItemFromArrayPiece",
        input_data=input_data
    )
    assert piece_output.get("output_value", None) in [1, 2, 3, 4, 5]


def test_getitemfromarray_another():
    input_data = dict(
        input_array=[1, 2, 3, 4, 5],
        index="another",
        another_index=3
    )
    piece_output = piece_dry_run(
        piece_name="GetItemFromArrayPiece",
        input_data=input_data
    )
    assert 4 == piece_output.get("output_value", None)
