from domino.testing import piece_dry_run


def test_pagescrapper():
    input_data = dict(
        url="https://en.wikipedia.org/wiki/Mr._Tambourine_Man",
        search_items=[
            dict(
                tag="article",
                class_name="",
            ),
            dict(
                tag="main",
                class_name="",
            ),
        ]
    )
    piece_output = piece_dry_run(
        piece_name="PageScrapperPiece",
        input_data=input_data
    )
    assert "tambourine" in piece_output["scrapped_text"].lower(), "PageScrapperPiece failed to scrap the page"
    assert "dylan" in piece_output["scrapped_text"].lower(), "PageScrapperPiece failed to scrap the page"
