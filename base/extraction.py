"""Abstract base class for PDF content extraction."""
from abc import ABC, abstractmethod

class Extraction(ABC):
    """Abstract base class for PDF extraction."""

    @abstractmethod
    def extract_content(self, pdf_path: str) -> str:
        """Extract content from a PDF and return it as a string."""

    def extract_and_save(self, pdf_path: str, output_path: str) -> None:
        """Extract content and save it to a text file."""
        content = self.extract_content(pdf_path)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Content saved to {output_path}")
