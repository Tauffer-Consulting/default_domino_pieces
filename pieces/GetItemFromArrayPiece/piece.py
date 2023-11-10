from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import random


class GetItemFromArrayPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        input_array = input_data.input_array
        index = input_data.index
        if index == 'first':
            output_value = input_array[0]
        elif index == 'last':
            output_value = input_array[-1]
        elif index == 'random':
            output_value = input_array[random.randint(0, len(input_array) - 1)]
        elif index == 'another':
            if input_data.another_index > len(input_array):
                raise ValueError(f"Index {input_data.another_index} is out of range for input array of length {len(input_array)}")
            output_value = input_array[input_data.another_index]

        self.logger.info(f"Output value: {output_value}")

        # Return output
        return OutputModel(
            output_value=output_value
        )
