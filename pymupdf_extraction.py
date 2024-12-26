"""Implementation of PDF content extraction using PyMuPDF."""
import fitz
from extraction import Extraction

class PyMuPDFExtraction(Extraction):
    """Extract content from the Unit-3 PDF using PyMuPDF."""

    def extract_content(self, pdf_path: str, output_path: str) -> None:
        with fitz.open(pdf_path) as pdf:
            with open(output_path, "w", encoding="utf-8") as output_file:
                for page in pdf:
                    output_file.write(page.get_text())
