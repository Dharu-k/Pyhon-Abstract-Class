"""Extract content from a PDF using PyMuPDF."""
import fitz
from base.extraction import Extraction

class PyMuPDFExtraction(Extraction):
    """Extract content from a PDF using PyMuPDF."""

    def extract_content(self, pdf_path: str) -> str:
        with fitz.open(pdf_path) as pdf:
            content = ""
            for page in pdf:
                content += page.get_text()
        return content
