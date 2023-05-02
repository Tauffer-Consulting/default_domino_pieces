from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import time
from pathlib import Path

class SimpleLogPiece(BasePiece):

    def piece_function(self, input_model: InputModel):
        # The BasePiece class provides a set of convenience self variables ready to be used
        secret_msg = f"""
        Example Piece secret: {self.secrets}
        """
        self.logger.info(secret_msg)

        # print("Sleeeping")
        # time.sleep(60)

        self.logger.info("Writing file to shared_storage")
        with open(str(Path(self.results_path)/"test.txt"), "w") as f:
            f.write("This is a test file")

        input_msg = f"""
        Example Piece input arguments: {input_model}
        """
        self.logger.info(input_msg)

        msg = """
        #############################################################################
        #############################################################################\n
        Example Piece Successfully Completed!\n
        #############################################################################\n
        #############################################################################
        """
        self.logger.info(msg)

        return OutputModel(
            message="Task successfully completed!",
            output_arg_1="something else"
        )