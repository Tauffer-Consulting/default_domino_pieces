from domino.base_piece import BasePiece
from io import BytesIO
from .models import InputModel, OutputModel
from pathlib import Path
from PIL import Image
import base64


class SaveImagePiece(BasePiece):
    def piece_function(self, input_data: InputModel):

        image_data_decoded = base64.decodebytes(input_data.base64_data.encode('utf-8'))
        img_buffer = BytesIO(image_data_decoded)
        img = Image.open(img_buffer)

        output_image_path = Path(self.results_path) / 'output_image.png'
        img.save(output_image_path)

        self.display_result = {
            "file_type": "image",
            "base64_content": input_data.base64_data,
            "file_path": str(output_image_path)
        }

        return OutputModel(
            output_image_path=str(output_image_path)
        )


        
        

        
    


