from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import importlib.util


class CustomPythonPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        # Log inputs
        self.logger.info(input_data.input_args)
        self.logger.info(input_data.output_args)
        self.logger.info(input_data.script)

        # Save the script as a local Python file
        script_file = "custom_script.py"
        with open(script_file, "w") as file:
            file.write(input_data.script)

        # Import the custom function from the script file
        spec = importlib.util.spec_from_file_location("custom_script", script_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Call the imported function with the input variables list
        output_args = getattr(module, "custom_function")(input_data.input_args)

        # Log output
        self.logger.info(output_args)

        # Return output
        return OutputModel(**output_args)