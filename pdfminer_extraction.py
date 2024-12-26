"""Implementation of PDF content extraction using PDFMiner."""
from pdfminer.high_level import extract_text
from extraction import Extraction

class PDFMinerExtraction(Extraction):
    """Extract content from the Unit-3 PDF using PDFMiner."""

    def extract_content(self, pdf_path: str, output_path: str) -> None:
        text = extract_text(pdf_path)
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(text)
