"""Main script to run the PDF content extraction."""
from pymupdf_extraction import PyMuPDFExtraction
from pdfminer_extraction import PDFMinerExtraction
from pypdf_extraction import PyPDF2Extraction

def main():
    """Run the content extraction."""
    pdf_path = "19225-UNIT 3-notes.pdf"
    output_path = "unit3_output.txt"

    print("Select an extraction method:")
    print("1. PyMuPDF")
    print("2. PDFMiner")
    print("3. PyPDF2")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        extractor = PyMuPDFExtraction()
    elif choice == "2":
        extractor = PDFMinerExtraction()
    elif choice == "3":
        extractor = PyPDF2Extraction()
    else:
        print("Invalid choice. Please select a valid option.")
        return

    extractor.extract_content(pdf_path, output_path)
    print(f"Content extracted and saved to {output_path}")

if __name__ == "__main__":
    main()
