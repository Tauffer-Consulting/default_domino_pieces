from pydantic import BaseModel, Field
from typing import List


class ItemType(BaseModel):
    tag: str = Field(
        default="p",
        description='HTML tag name.',
    )
    class_name: str = Field(
        default="",
        description='HTML tag class name.',
    )


class InputModel(BaseModel):
    """
    PageScrapperPiece Input Model
    """
    url: str = Field(
        default="",
        description='URL to retrieve content from.'
    )
    search_items: List[ItemType] = Field(
        default=[ItemType()],
        description='List of HTML tags and class names to search for.'
    )


class OutputModel(BaseModel):
    """
    PageScrapperPiece Output Model
    """
    scrapped_text: str = Field(
        description='Scrapped text from the URL.'
    )
