import fitz
import os

pdf_path = "TheoryOfComputation.pdf"  # Assuming the PDF is in the same directory

try:
    pdf = fitz.open(pdf_path)

    # Improved text extraction with block-wise approach
    extracted_text = ""
    for page_number in range(len(pdf)):
        page = pdf.load_page(page_number)
        blocks = page.get_text("blocks")  # Extract text in blocks for better formatting

        for block in blocks:
            extracted_text += block[4]  # Access text content (index 4) within each block
            extracted_text += "\n"  # Add newline for readability

    # Enhanced output handling
    output_filename = os.path.splitext(pdf_path)[0] + "_extracted_text.txt"  # Generate filename based on original PDF name
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(extracted_text)

    print(f"Text successfully extracted from '{pdf_path}' and saved to '{output_filename}'.")

    pdf.close()

except FileNotFoundError:
    print(f"Error: '{pdf_path}' not found. Please check the file path.")