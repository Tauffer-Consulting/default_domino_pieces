from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import lorem


class LoremIpsumGeneratorPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        items = input_data.items
        number_of_items = input_data.number_of_items

        output_text = ""
        if items == "words":
            output_text = lorem.get_word(number_of_items)
        elif items == "sentences":
            output_text = lorem.get_sentence(number_of_items)
        elif items == "paragraphs":
            output_text = lorem.get_paragraph(number_of_items)

        self.logger.info(f"Generated text: {output_text}")
        self.format_display_result(input_data, output_text)

        # Return output
        return OutputModel(
            output_text=output_text
        )

    def format_display_result(self, input_data: InputModel, output_text: str):
        md_text = "Lorem Ipsum Generator Piece\n"
        md_text += "============================\n\n"
        md_text += "**Input data:**\n"
        md_text += f"items: {input_data.items}\n"
        md_text += f"number_of_items: {input_data.number_of_items}\n\n"
        md_text += "**Output data:**\n"
        md_text += f"output_text: {output_text}\n\n"
        file_path = f"{self.results_path}/display_result.md"
        with open(file_path, "w") as f:
            f.write(md_text)
        self.display_result = {
            "file_type": "md",
            "file_path": file_path
        }
