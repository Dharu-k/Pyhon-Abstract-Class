"""Factory module for PDF extraction classes."""
from pdf_extractors.pdfminer_extraction import PDFMinerExtraction
from pdf_extractors.pymupdf_extraction import PyMuPDFExtraction
from pdf_extractors.pypdf_extraction import PyPDF2Extraction

class ExtractionFactory:
    """Factory to instantiate the appropriate PDF extraction class."""

    METHOD_MAP = {
        "PDFMiner": PDFMinerExtraction,
        "PyMuPDF": PyMuPDFExtraction,
        "PyPDF2": PyPDF2Extraction,
    }

    @staticmethod
    def create_extraction(method: str):
        """Create an instance of the appropriate extraction class."""
        try:
            return ExtractionFactory.METHOD_MAP[method]()
        except KeyError as exc:
            raise ValueError(f"Unsupported extraction method: {method}") from exc
