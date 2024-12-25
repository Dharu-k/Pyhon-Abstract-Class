"""This module provides an abstract base class for PDF content extraction."""

from abc import ABC, abstractmethod

class Extraction(ABC):
    """Abstract base class for PDF content extraction."""

    @abstractmethod
    def extract_content(self, pdf_path: str, output_path: str) -> None:
        """Extract contents from unit-3 PDF file."""
