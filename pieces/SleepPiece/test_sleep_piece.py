from domino.testing import piece_dry_run
from datetime import datetime


def test_sleep_piece():
    sleep_time = 1
    input_data = dict(
        sleep_time=sleep_time
    )
    start_time = datetime.now()
    piece_output = piece_dry_run(
        piece_name="SleepPiece",
        input_data=input_data
    )
    end_time = datetime.now()
    assert (end_time - start_time).total_seconds() >= sleep_time
    assert 'message' in piece_output
