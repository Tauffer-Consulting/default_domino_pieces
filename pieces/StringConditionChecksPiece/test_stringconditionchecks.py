from domino.testing import piece_dry_run


def test_stringconditionchecks_1():
    check_1 = dict(
        operation='contains_case_sensitive',
        second_argument='world',
        next_logical_operator='and',
    )
    check_2 = dict(
        operation='contains_case_insensitive',
        second_argument='hello',
        next_logical_operator='and',
    )
    check_3 = dict(
        operation='length_greater_than',
        second_argument='5',
        next_logical_operator='and',
    )
    check_4 = dict(
        operation='length_less_than',
        second_argument='30',
        next_logical_operator='and',
    )
    check_5 = dict(
        operation='length_equal_to',
        second_argument='19',
        next_logical_operator='and',
    )
    check_6 = dict(
        operation='regex_match',
        second_argument='.*Domino.*$',
    )
    input_data = dict(
        input_string='Hello Domino world!',
        operations=[check_1, check_2, check_3, check_4, check_5, check_6]
    )
    piece_output = piece_dry_run(
        piece_name="StringConditionChecksPiece",
        input_data=input_data
    )
    assert piece_output.get("check_result", False)


def test_stringconditionchecks_2():
    check_1 = dict(
        operation='length_greater_than_or_equal_to',
        second_argument='90',
        next_logical_operator='or',
    )
    check_2 = dict(
        operation='length_less_than_or_equal_to',
        second_argument='1',
    )
    input_data = dict(
        input_string='Hello Domino world!',
        operations=[check_1, check_2]
    )
    piece_output = piece_dry_run(
        piece_name="StringConditionChecksPiece",
        input_data=input_data
    )
    assert not piece_output.get("check_result", True)
