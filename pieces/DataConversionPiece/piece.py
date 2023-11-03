from domino.base_piece import BasePiece
from pathlib import Path
from io import StringIO
import pandas as pd
from .models import InputModel, OutputModel, DataFormatOption


class DataConversionPiece(BasePiece):
    def piece_function(self, input_data: InputModel):
        # Convert input data type to output data type
        data = input_data.input_data

        # Check if input data is a file path
        if Path(data).is_file():
            if input_data.input_data_format == DataFormatOption.csv:
                df = pd.read_csv(data)
            elif input_data.input_data_format == DataFormatOption.json:
                df = pd.read_json(data)
        else:
            if input_data.input_data_format == DataFormatOption.csv:
                csv_stringio = StringIO(data)
                df = pd.read_csv(csv_stringio, sep=',', index_col=0)
            elif input_data.input_data_format == DataFormatOption.json:
                df = pd.read_json(data)
        
        # Convert to output data type
        if input_data.output_data_format == DataFormatOption.csv:
            output_path = Path(self.results_path) / 'output.csv'
            df.to_csv(str(output_path))
        elif input_data.output_data_format == DataFormatOption.json:
            output_path = Path(self.results_path) / 'output.json'
            df.to_json(str(output_path))

        output = OutputModel(
            output_file_path=str(output_path)
        )
        return output
    


