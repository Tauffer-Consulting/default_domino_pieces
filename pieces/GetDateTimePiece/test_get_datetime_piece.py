from domino.testing import piece_dry_run
from datetime import datetime


def test_get_datetime_piece():
    input_data = dict(
        use_timezone=True,
        timezone='(UTC-03) - Canada/Atlantic'
    )

    piece_output = piece_dry_run(
        repository_folder_path=".",
        piece_name="GetDateTimePiece",
        input_data=input_data
    )

    assert 'date' in piece_output
    assert 'time' in piece_output
    assert 'datetime' in piece_output

    assert piece_output['date'] == datetime.now().date().isoformat()
    dt = datetime.fromisoformat(piece_output['datetime'])
    timezone = dt.tzinfo
    assert str(timezone) in ['UTC-03:00', 'UTC-04:00'] # Using list because of DST 

    