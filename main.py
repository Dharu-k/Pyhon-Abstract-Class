"""Extract content from a PDF."""
from extraction import Extraction  # Importing the abstract class
from pymupdf_extraction import PyMuPDFExtraction
from pdfminer_extraction import PDFMinerExtraction
from pypdf_extraction import PyPDF2Extraction
METHOD_MAP = {
    "PyMuPDF": PyMuPDFExtraction,
    "PDFMiner": PDFMinerExtraction,
    "PyPDF2": PyPDF2Extraction,
}
def create_extraction(method: str) -> Extraction:
    """Factory method to instantiate the appropriate extraction class."""
    try:
        return METHOD_MAP[method](method)  
    except KeyError as exc:
        raise ValueError(f"Unsupported extraction method: {method}") from exc
def main():
    """Run the content extraction."""
    pdf_path = "19225-UNIT 3-notes.pdf"  # Input PDF
    output_path = "unit3_output.txt"    # Output text file
    print("Select an extraction method:")
    print("1. PyMuPDF")
    print("2. PDFMiner")
    print("3. PyPDF2")
    choice = input("Enter your choice (1/2/3): ")
    # Map user choice to extraction method
    methods = {"1": "PyMuPDF", "2": "PDFMiner", "3": "PyPDF2"}
    method = methods.get(choice)
    if not method:
        print("Invalid choice. Exiting.")
        return
    # Instantiate the extraction class (passing the extraction type)
    extractor = create_extraction(method)
    # Use the method from the abstract class to extract and save content
    extractor.extract_and_save(pdf_path, output_path)
if __name__ == "__main__":
    main()
