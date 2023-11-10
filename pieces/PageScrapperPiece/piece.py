from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import requests
from bs4 import BeautifulSoup
import re
from html import unescape


def clean_text(text):
    # Replace HTML entities with their corresponding characters, e.g., '&amp;' becomes '&'
    text = unescape(text)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Replace sequences of whitespace characters with a single space
    text = re.sub(r'\s+', ' ', text)
    # Remove leading and trailing whitespace
    text = text.strip()
    # Remove other unwanted characters
    text = text.replace(u'\xa0', ' ').replace('\r', '').replace('\n', '').replace('\t', '').replace('\u200b', '')
    return text


def extract_content_with_known_tags_classes(url, search_items):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = []
        for item in search_items:
            if item.class_name:
                elements = soup.find_all(item.tag, class_=item.class_name)
            else:
                elements = soup.find_all(item.tag)
            for element in elements:
                content.append(element.get_text(separator=' ', strip=True))
        return clean_text(' '.join(content))
    else:
        return ""


class PageScrapperPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        url = input_data.url
        search_items = input_data.search_items

        self.logger.info("Starting page scrapper...")
        self.logger.info(f"URL: {url}")
        self.logger.info(f"Search items: {search_items}")

        content = extract_content_with_known_tags_classes(url, search_items)

        self.logger.info(f"Scrapped text: {content}")

        # Return output
        return OutputModel(
            scrapped_text=content,
        )

    def format_display_result(self, input_data: InputModel, content: str):
        md_text = f"**url:** {input_data.url}\n"
        for item in input_data.search_items:
            md_text += f"**tag:** {item['tag']} \t**class_name:** {item['class_name']}\n"
        md_text += f"**scrapped text:**\n{content}\n"
        file_path = f"{self.results_path}/display_result.md"
        with open(file_path, "w") as f:
            f.write(md_text)
        self.display_result = {
            "file_type": "md",
            "file_path": file_path
        }
