"""Implementation of PDF content extraction using PyMPDF2."""
from PyPDF2 import PdfReader
from extraction import Extraction

class PyPDF2Extraction(Extraction):
    """Extract content from the Unit-3 PDF using PyPDF2."""

    def extract_content(self, pdf_path: str, output_path: str) -> None:
        reader = PdfReader(pdf_path)
        with open(output_path, "w", encoding="utf-8") as output_file:
            for page in reader.pages:
                output_file.write(page.extract_text())
