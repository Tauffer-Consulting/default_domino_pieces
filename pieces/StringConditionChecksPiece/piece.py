from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from pathlib import Path
import re


def apply_logical_operations(checks, logical_operations):
    if len(logical_operations) != len(checks) - 1:
        raise ValueError("Number of logical operations should be one less than the number of checks")
    result = checks[0]
    for i in range(len(logical_operations)):
        operation = logical_operations[i]
        next_value = checks[i + 1]
        if operation == "and":
            result = result and next_value
        elif operation == "or":
            result = result or next_value
        else:
            raise ValueError(f"Unsupported logical operation: {operation}")
    return result


class StringConditionChecksPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        input_string = input_data.input_string
        operations_array = input_data.operations
        msg = f"Input string: '{input_string}'\n\n"
        msg += "Operations:\n"
        checks_values = []
        logical_operations = []
        for operation_item in operations_array:
            operation = operation_item.operation
            second_argument = operation_item.second_argument
            next_logical_operator = operation_item.next_logical_operator.value
            logical_operations.append(next_logical_operator)
            msg += f"{operation.value}: '{second_argument}'\n"
            msg += f"{next_logical_operator}\n"
            if operation == 'contains_case_sensitive':
                if second_argument in input_string:
                    checks_values.append(True)
                else:
                    checks_values.append(False)
            elif operation == 'contains_case_insensitive':
                if second_argument.lower() in input_string.lower():
                    checks_values.append(True)
                else:
                    checks_values.append(False)
            elif operation == 'length_greater_than':
                if len(input_string) > int(second_argument):
                    checks_values.append(True)
                else:
                    checks_values.append(False)
            elif operation == 'length_greater_than_or_equal_to':
                if len(input_string) >= int(second_argument):
                    checks_values.append(True)
                else:
                    checks_values.append(False)
            elif operation == 'length_less_than':
                if len(input_string) < int(second_argument):
                    checks_values.append(True)
                else:
                    checks_values.append(False)
            elif operation == 'length_less_than_or_equal_to':
                if len(input_string) <= int(second_argument):
                    checks_values.append(True)
                else:
                    checks_values.append(False)
            elif operation == 'length_equal_to':
                if len(input_string) == int(second_argument):
                    checks_values.append(True)
                else:
                    checks_values.append(False)
            elif operation == 'regex_match':
                if re.match(second_argument, input_string):
                    checks_values.append(True)
                else:
                    checks_values.append(False)

        # Evaluate logical operations
        logical_operations = logical_operations[:-1]
        result = apply_logical_operations(checks_values, logical_operations)

        msg += "(last logical operation is ignored)\n"
        msg += f"\nFinal result: {result}"
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
            check_result=result,
        )
