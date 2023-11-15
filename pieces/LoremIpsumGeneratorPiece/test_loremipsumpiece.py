from domino.testing import piece_dry_run


def test_loremipsumpiece():
    input_data = dict(
        items="words",
        number_of_items=10
    )
    piece_output = piece_dry_run(
        piece_name="LoremIpsumGeneratorPiece",
        input_data=input_data
    )
    assert len(piece_output["output_text"].split()) == 10
