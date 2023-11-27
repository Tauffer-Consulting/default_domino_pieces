from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from pathlib import Path


class StringOperationsPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        first_argument = input_data.first_argument
        operations_array = input_data.operations
        msg = "Operations:\n"
        for operation_item in operations_array:
            operation = operation_item.operation
            second_argument = operation_item.second_argument
            auxiliary_argument = operation_item.auxiliary_argument
            msg += f"{operation.value}: '{first_argument}' | '{second_argument}' | '{auxiliary_argument}'\n"
            if operation == 'split_by':
                try:
                    index = int(auxiliary_argument)
                    first_argument = first_argument.split(second_argument)[index]
                except ValueError:
                    raise ValueError('Auxiliary argument must be an integer when using `split_by` operation')
                except IndexError:
                    raise IndexError('Index out of range when using `split_by` operation')
            elif operation == 'replace_by':
                first_argument = first_argument.replace(second_argument, auxiliary_argument)
            elif operation == 'concatenate':
                first_argument = first_argument + second_argument
            elif operation == 'lower_case':
                first_argument = first_argument.lower()
            elif operation == 'upper_case':
                first_argument = first_argument.upper()
            elif operation == 'strip_spaces':
                first_argument = first_argument.strip()

        msg += f"\nOutput: {first_argument}"
        self.logger.info(msg)

        # Set display result
        file_path = str(Path(self.results_path)/"log.txt")
        with open(file_path, "w") as f:
            f.write(msg)

        self.display_result = {
            "file_type": "txt",
            "file_path": file_path
        }

        return OutputModel(
            output_string=first_argument,
        )
