from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from pathlib import Path


class CustomPythonPiece(BasePiece):

    def piece_function(self, input_model: InputModel):
        # Log inputs
        self.logger.info(input_model.input_args)
        self.logger.info(input_model.output_args)
        self.logger.info(input_model.script)

        # Write log file
        # self.logger.info("Writing log file to shared_storage...")
        # file_path = str(Path(self.results_path)/"log.txt")
        # with open(file_path, "w") as f:
        #     f.write(msg)

        # Set display result
        # self.display_result = {
        #     "file_type": "txt",
        #     "file_path": file_path
        # }

        # Return output
        return OutputModel(
            error=None,
        )