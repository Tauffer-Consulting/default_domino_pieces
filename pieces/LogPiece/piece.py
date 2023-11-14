from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from pathlib import Path


class LogPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        # Log inputs
        msg = f"""## Log Piece: \n\n
Input string: {input_data.input_str}\n
Input integer: {input_data.input_int}\n
Input float: {input_data.input_float}\n
Input boolean: {input_data.input_bool}\n
Input array: {input_data.input_array}\n
Input enum: {input_data.input_enum}\n
Input date: {input_data.input_date}\n
Input time: {input_data.input_time}\n
Input datetime: {input_data.input_datetime}\n
Input code: {input_data.input_code}\n
"""
        self.logger.info(msg)

        # Write log file
        self.logger.info("Writing log file to shared_storage...")
        file_path = str(Path(self.results_path)/"log.txt")
        with open(file_path, "w") as f:
            f.write(msg)

        # Set display result
        self.display_result = {
            "file_type": "txt",
            "file_path": file_path
        }

        # Return output
        return OutputModel(
            output_log=msg,
            output_str=input_data.input_str,
            output_int=input_data.input_int,
            output_float=input_data.input_float,
            output_bool=input_data.input_bool,
            output_enum=input_data.input_enum,
            output_array=input_data.input_array,
            output_date=input_data.input_date,
            output_time=input_data.input_time,
            output_datetime=input_data.input_datetime,
            output_code=input_data.input_code
        )
