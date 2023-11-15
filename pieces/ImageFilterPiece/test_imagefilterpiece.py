from domino.testing import piece_dry_run
from pathlib import Path
from PIL import Image
from io import BytesIO
import base64


# Open test image and convert to base64 string using Pillow
img_path = str(Path(__file__).parent / "test_image.png")
img = Image.open(img_path)
buffered = BytesIO()
img.save(buffered, format="PNG")
image_bytes = buffered.getvalue()
base64_image = base64.b64encode(image_bytes).decode("utf-8")


def test_imagefilterpiece():
    input_data = dict(
        input_image=base64_image,
        sepia=True,
        blue=True,
        output_type="both"
    )
    piece_output = piece_dry_run(
        piece_name="ImageFilterPiece",
        input_data=input_data
    )
    assert piece_output is not None
    assert piece_output.get('image_file_path').endswith('.png')
