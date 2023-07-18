from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from datetime import datetime
import pytz
import base64


class GetDateTimePiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        
        if input_data.use_timezone:
            timezone = input_data.timezone
            timezone = timezone.split(' - ')[0].replace('(', '').replace(')', '').strip()
            timezone = pytz.timezone(timezone)
            date = datetime.now(timezone).date().isoformat()
            time = datetime.now(timezone).time().isoformat()
            datetime_ = datetime.now(timezone).isoformat()
        else:
            date = datetime.now().date().isoformat()
            time = datetime.now().time().isoformat()
            datetime_ = datetime.now().isoformat()

        self.logger.info(f"Date: {date}\nTime: {time}\nDatetime: {datetime_}")

        # Set display result
        raw_content = f"Date: {date}\Time: {time}\nDatetime: {datetime_}"
        base64_content = base64.b64encode(raw_content.encode("utf-8")).decode("utf-8")
        self.display_result = {
            "file_type": "txt",
            "base64_content": base64_content
        }

        # Return output
        return OutputModel(
            date=date,
            time=time,
            datetime=datetime_
        )