"""Main script to run the PDF content extraction."""

from pymupdf_extraction import PyMuPDFExtraction

def main():
    """Run the content extraction."""
    pdf_path = "19225-UNIT 3-notes.pdf" 
    output_path = "unit3_output.txt"   

    extractor = PyMuPDFExtraction()
    extractor.extract_content(pdf_path, output_path)
    print(f"Content extracted and saved to {output_path}")
if __name__ == "__main__":
    main()
