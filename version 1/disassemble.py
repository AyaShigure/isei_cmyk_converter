import fitz  # PyMuPDF
from PIL import Image
import os

def pdf_to_jpegs(pdf_path, output_folder, dpi=600):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each page in the PDF
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        
        # Render the page to an image (pixmap)
        zoom = dpi / 30  # dpi scaling factor
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)

        # Convert the pixmap to an image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Save the image as a JPEG file
        output_path = os.path.join(output_folder, f"page_{page_number + 1}.jpg")
        img.save(output_path, "JPEG", quality=95)
        print(f"Saved {output_path}")

if __name__ == "__main__":
    input_pdf_path = "test.pdf"  # Replace with your input PDF file path
    output_folder = "output_images"  # Replace with your target folder

    pdf_to_jpegs(input_pdf_path, output_folder)
