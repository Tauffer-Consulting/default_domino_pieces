from domino.testing import piece_dry_run


def test_stringoperationpiece_1():
    operation_1 = dict(
        operation='concatenate',
        second_argument=' world ',
    )
    operation_2 = dict(
        operation='strip_spaces',
    )
    operation_3 = dict(
        operation='replace_by',
        second_argument='world',
        auxiliary_argument='DOMINO!',
    )
    operation_4 = dict(
        operation='lower_case',
    )
    input_data = dict(
        first_argument='Hello',
        operations=[operation_1, operation_2, operation_3, operation_4]
    )
    piece_output = piece_dry_run(
        piece_name="StringOperationsPiece",
        input_data=input_data
    )
    assert piece_output.get("output_string", "") == "hello domino!"


def test_stringoperationpiece_2():
    operation_1 = dict(
        operation='upper_case',
    )
    operation_2 = dict(
        operation='split_by',
        second_argument=' ',
        auxiliary_argument='1',
    )
    operation_3 = dict(
        operation='concatenate',
        second_argument='!',
    )
    input_data = dict(
        first_argument='never gonna give you up',
        operations=[operation_1, operation_2, operation_3]
    )
    piece_output = piece_dry_run(
        piece_name="StringOperationsPiece",
        input_data=input_data
    )
    assert piece_output.get("output_string", "") == "GONNA!"
