from domino.testing import piece_dry_run
from datetime import datetime
import re
from datetime import datetime


def validate_iso_format(s):
    # Regular expressions for ISO date, time, and datetime formats
    date_regex = r'^\d{4}-\d{2}-\d{2}$'
    time_regex = r'^\d{2}:\d{2}:\d{2}(\.\d+)?$'
    datetime_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?$'

    if re.match(date_regex, s):
        return True
    elif re.match(time_regex, s):
        return True
    elif re.match(datetime_regex, s):
        return True
    else:
        return False


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

    assert validate_iso_format(piece_output['date'])
    assert validate_iso_format(piece_output['time'])
    assert validate_iso_format(piece_output['datetime'])

    dt = datetime.fromisoformat(piece_output['datetime'])
    timezone = dt.tzinfo
    assert str(timezone) in ['UTC-03:00', 'UTC-04:00']  # Using list because of DST
