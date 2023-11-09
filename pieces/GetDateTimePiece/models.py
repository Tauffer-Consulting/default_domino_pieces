from pydantic import BaseModel, Field
from enum import Enum
from datetime import date as dt_date, datetime as dt_datetime, time as dt_time


class TZOptions(str, Enum):
    utc_minus_11 = '(UTC-11) - Pacific/Pago_Pago'
    utc_minus_10 = '(UTC-10) - US/Hawaii'
    utc_minus_09 = '(UTC-09) - Pacific/Gambier'
    utc_minus_08 = '(UTC-08) - US/Alaska'
    utc_minus_07 = '(UTC-07) - US/Pacific'
    utc_minus_06 = '(UTC-06) - US/Mountain'
    utc_minus_05 = '(UTC-05) - US/Central'
    utc_minus_04 = '(UTC-04) - US/Eastern'
    utc_minus_03 = '(UTC-03) - Canada/Atlantic'
    utc_minus_02 = '(UTC-02) - Atlantic/South_Georgia'
    utc_minus_01 = '(UTC-01) - Atlantic/Cape_Verde'
    utc_plus_00 = '(UTC+00) - UTC'
    utc_plus_01 = '(UTC+01) - Europe/London'
    utc_plus_02 = '(UTC+02) - Europe/Zurich'
    utc_plus_03 = '(UTC+03) - Indian/Mayotte'
    utc_plus_04 = '(UTC+04) - Asia/Tehran'
    utc_plus_05 = '(UTC+05) - Asia/Kathmandu'
    utc_plus_06 = '(UTC+06) - Indian/Cocos'
    utc_plus_07 = '(UTC+07) - Indian/Christmas'
    utc_plus_08 = '(UTC+08) - Australia/Eucla'
    utc_plus_09 = '(UTC+09) - Australia/Darwin'
    utc_plus_10 = '(UTC+10) - Australia/Lord_Howe'
    utc_plus_11 = '(UTC+11) - Pacific/Pohnpei'
    utc_plus_12 = '(UTC+12) - Pacific/Chatham'
    utc_plus_13 = '(UTC+13) - Pacific/Tongatapu'
    utc_plus_14 = '(UTC+14) - Pacific/Kiritimati'


class InputModel(BaseModel):
    """
    GetDateTimePiece Input Model
    """
    use_timezone: bool = Field(
        default=False,
        description='Whether to use a timezone for the timestamp.'
    )
    timezone: TZOptions = Field(
        default=TZOptions.utc_plus_00,
        description='Timezone to use for timestamp.'
    )


class OutputModel(BaseModel):
    """
    GetDateTimePiece Output Model
    """
    date: dt_date = Field(
        description='Date of the timestamp, in ISO format.'
    )
    time: dt_time = Field(
        description='Time of the timestamp, in ISO format.'
    )
    datetime: dt_datetime = Field(
        description='Datetime of the timestamp, in ISO format.'
    )