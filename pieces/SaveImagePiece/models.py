from pydantic import BaseModel, Field



class InputModel(BaseModel):
    base64_data: str = Field(
        description='Input data to be saved as image.'
    )


class OutputModel(BaseModel):
    output_image_path: str = Field(
        description='Output file path of the saved image.'
    )