"""This module provides an abstract base class for PDF content extraction."""
from abc import ABC, abstractmethod

class Extraction(ABC):
    """Abstract base class for PDF extraction."""

    @abstractmethod
    def extract_content(self, pdf_path: str, output_path: str) -> None:
        """Extract content from Unit-3 PDF file and save it to a text file."""
