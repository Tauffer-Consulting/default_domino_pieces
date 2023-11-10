from domino.testing import piece_dry_run


def test_pagescrapper():
    input_data = dict(
        url="https://www.bobdylan.com/songs/mr-tambourine-man/",
        search_items=[
            dict(
                tag="article",
                class_name="",
            )
        ]
    )
    piece_output = piece_dry_run(
        piece_name="PageScrapperPiece",
        input_data=input_data
    )
    assert "tambourine" in piece_output["scrapped_text"].lower(), "PageScrapperPiece failed to scrap the page"
    assert "dylan" in piece_output["scrapped_text"].lower(), "PageScrapperPiece failed to scrap the page"
