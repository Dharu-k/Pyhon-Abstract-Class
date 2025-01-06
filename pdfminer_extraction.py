"""Extract content from a PDF using PDFMiner."""
from pdfminer.high_level import extract_text
from base.extraction import Extraction

class PDFMinerExtraction(Extraction):
    """Extract content from a PDF using PDFMiner."""

    def extract_content(self, pdf_path: str) -> str:
        return extract_text(pdf_path)
