from pydantic import BaseModel, Field
from enum import Enum


class ItemsType(str, Enum):
    words = 'words'
    sentences = 'sentences'
    paragraphs = 'paragraphs'


class InputModel(BaseModel):
    """
    LoremIpsumGeneratorPiece Input Model
    """
    items: ItemsType = Field(
        default=ItemsType.words,
        description="Type of items to generate.",
    )
    number_of_items: int = Field(
        default=1,
        description="Number of items to generate.",
    )


class OutputModel(BaseModel):
    """
    LoremIpsumGeneratorPiece Output Model
    """
    output_text: str = Field(
        description="Generated text."
    )
