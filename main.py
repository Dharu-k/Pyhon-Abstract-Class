"""Main script to extract content from a PDF."""
from factory.extraction_factory import ExtractionFactory

def main():
    """Run the content extraction process."""
    pdf_path = "19225-UNIT 3-notes.pdf"  # Input PDF
    output_path = "unit3_output.txt"      # Output text file

    print("Select an extraction method:")
    print("1. PyMuPDF")
    print("2. PDFMiner")
    print("3. PyPDF2")

    choice = input("Enter your choice (1/2/3): ")
    methods = {"1": "PyMuPDF", "2": "PDFMiner", "3": "PyPDF2"}
    method = methods.get(choice)

    if not method:
        print("Invalid choice. Exiting.")
        return

    try:
        extractor = ExtractionFactory.create_extraction(method)
        extractor.extract_and_save(pdf_path, output_path)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
