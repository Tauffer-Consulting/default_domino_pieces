from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from time import sleep


class SleepPiece(BasePiece):

    def piece_function(self, input_model: InputModel):

        self.logger.info(f"Sleeping for {input_model.sleep_time} seconds")
        sleep(input_model.sleep_time)

        message = f"Sleep piece executed successfully for {input_model.sleep_time} seconds"

        # Return output
        return OutputModel(
            message=message,
        )