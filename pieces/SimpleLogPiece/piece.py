from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from pathlib import Path


class SimpleLogPiece(BasePiece):

    def piece_function(self, input_model: InputModel):
        # Log inputs
        msg = f"""
#############################################################################\n
Logged inputs:\n
Input string: {input_model.input_str}\n
Input integer: {input_model.input_int}\n
Input float: {input_model.input_float}\n
Input boolean: {input_model.input_bool}\n
Input list: {input_model.input_list}\n
Input enum: {input_model.input_enum}\n
Input date: {input_model.input_date}\n
Input time: {input_model.input_time}\n
Input datetime: {input_model.input_datetime}\n
Input code: {input_model.input_code}\n
#############################################################################\n
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
            message="Task successfully completed!",
            output_msg=msg
        )