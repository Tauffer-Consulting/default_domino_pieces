import pandas as pd
from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from pathlib import Path
from ydata_profiling import ProfileReport


class YDataProfilingPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        df = pd.read_csv(input_data.data_path)

        profile = ProfileReport(df, title=input_data.report_tile)

        file_path = str(Path(self.results_path) / 'report.html')
        profile.to_file(file_path)

        self.display_result = {
            "file_path": file_path,
            "file_type": "html"
        }

        return OutputModel(
            profile_file_path=file_path
        )

