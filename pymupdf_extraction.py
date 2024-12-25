"""Implementation of PDF content extraction using PyMuPDF."""

import fitz
from Extraction import Extraction

class PyMuPDFExtraction(Extraction):
    """Class to extract content from My PDF using PyMuPDF."""

    def extract_content(self, pdf_path: str, output_path: str) -> None:
        """Extract content from My PDF and save it to a text file."""
        with fitz.open(pdf_path) as pdf:
            with open(output_path, 'w', encoding='utf-8') as output_file:
                for page in pdf:
                    output_file.write(page.get_text())
