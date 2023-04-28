from flowui.base_operator import BaseOperator
from .models import InputModel, OutputModel
import time
from pathlib import Path

class ExampleOperator(BaseOperator):

    def operator_function(self, input_model: InputModel):
        # The BaseOperator class provides a set of convenience self variables ready to be used
        secret_msg = f"""
        Example Operator secret: {self.secrets}
        """
        self.logger.info(secret_msg)

        self.logger.info("Writing file to shared_storage")
        with open(str(Path(self.workflow_shared_storage)/"test.txt"), "w") as f:
            f.write("This is a test file")

        time.sleep(5)

        input_msg = f"""
        Example Operator input arguments: {input_model}
        """
        self.logger.info(input_msg)

        msg = """
        #############################################################################
        #############################################################################\n
        Example Operator Successfully Completed!\n
        #############################################################################\n
        #############################################################################
        """
        self.logger.info(msg)

        return OutputModel(
            message="Task successfully completed!",
            output_arg_1="something else"
        )