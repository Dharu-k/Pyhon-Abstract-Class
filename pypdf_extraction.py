"""Extract content from a PDF using PyPDF2."""
from PyPDF2 import PdfReader
from extraction import Extraction
class PyPDF2Extraction(Extraction):
    """Extract content from a PDF using PyPDF2."""
    def extract_content(self, pdf_path: str) -> str:
        reader = PdfReader(pdf_path)
        content = ""
        for page in reader.pages:
            content += page.extract_text()
        return content
    