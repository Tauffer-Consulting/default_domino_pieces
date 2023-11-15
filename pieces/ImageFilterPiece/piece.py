from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from pathlib import Path
from PIL import Image
from io import BytesIO
import numpy as np
import base64
import os


filter_masks = {
    'sepia': ((0.393, 0.769, 0.189), (0.349, 0.686, 0.168), (0.272, 0.534, 0.131)),
    'black_and_white': ((0.333, 0.333, 0.333), (0.333, 0.333, 0.333), (0.333, 0.333, 0.333)),
    'brightness': ((1.4, 0, 0), (0, 1.4, 0), (0, 0, 1.4)),
    'darkness': ((0.6, 0, 0), (0, 0.6, 0), (0, 0, 0.6)),
    'contrast': ((1.2, 0.6, 0.6), (0.6, 1.2, 0.6), (0.6, 0.6, 1.2)),
    'red': ((1.6, 0, 0), (0, 1, 0), (0, 0, 1)),
    'green': ((1, 0, 0), (0, 1.6, 0), (0, 0, 1)),
    'blue': ((1, 0, 0), (0, 1, 0), (0, 0, 1.6)),
    'cool': ((0.9, 0, 0), (0, 1.1, 0), (0, 0, 1.3)),
    'warm': ((1.2, 0, 0), (0, 0.9, 0), (0, 0, 0.8)),
}


class ImageFilterPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        apply_sepia = input_data.sepia
        apply_black_and_white = input_data.black_and_white
        apply_brightness = input_data.brightness
        apply_darkness = input_data.darkness
        apply_contrast = input_data.contrast
        apply_red = input_data.red
        apply_green = input_data.green
        apply_blue = input_data.blue
        apply_cool = input_data.cool
        apply_warm = input_data.warm

        all_filters = list()
        if apply_sepia:
            all_filters.append('sepia')
        if apply_black_and_white:
            all_filters.append('black_and_white')
        if apply_brightness:
            all_filters.append('brightness')
        if apply_darkness:
            all_filters.append('darkness')
        if apply_contrast:
            all_filters.append('contrast')
        if apply_red:
            all_filters.append('red')
        if apply_green:
            all_filters.append('green')
        if apply_blue:
            all_filters.append('blue')
        if apply_cool:
            all_filters.append('cool')
        if apply_warm:
            all_filters.append('warm')

        # Try to open image from file path or base64 encoded string
        input_image = input_data.input_image

        max_path_size = int(os.pathconf('/', 'PC_PATH_MAX'))
        if len(input_image) < max_path_size and Path(input_image).exists() and Path(input_image).is_file():
            image = Image.open(input_image)
        else:
            self.logger.info("Input image is not a file path, trying to decode as base64 string")
            try:
                decoded_data = base64.b64decode(input_image)
                image_stream = BytesIO(decoded_data)
                image = Image.open(image_stream)
                image.verify()
                image = Image.open(image_stream)
            except Exception:
                raise ValueError("Input image is not a file path or a base64 encoded string")


        # Convert Image to NumPy array
        np_image = np.array(image, dtype=float)

        # Apply filters
        self.logger.info(f"Applying filters: {', '.join(all_filters)}")
        for filter_name in all_filters:
            np_mask = np.array(filter_masks[filter_name], dtype=float)
            for y in range(np_image.shape[0]):
                for x in range(np_image.shape[1]):
                    rgb = np_image[y, x, :3]
                    new_rgb = np.dot(np_mask, rgb)
                    np_image[y, x, :3] = new_rgb
            # Clip values to be in valid range
            np_image = np.clip(np_image, 0, 255)

        # Convert back to uint8 and PIL image
        np_image = np_image.astype(np.uint8)
        modified_image = Image.fromarray(np_image)

        # Save to file
        image_file_path = ""
        if input_data.output_type == "file" or input_data.output_type == "both":
            image_file_path = f"{self.results_path}/modified_image.png"
            modified_image.save(image_file_path)

        # Convert to base64 string
        image_base64_string = ""
        if input_data.output_type == "base64_string" or input_data.output_type == "both":
            buffered = BytesIO()
            modified_image.save(buffered, format="PNG")
            image_base64_string = base64.b64encode(buffered.getvalue()).decode('utf-8')


        self.display_result = {
            "file_type": "png",
            "base64_content": image_base64_string,
            "file_path": image_file_path
        }

        # Return output
        return OutputModel(
            image_base64_string=image_base64_string,
            image_file_path=image_file_path,
        )
