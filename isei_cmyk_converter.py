import fitz  # PyMuPDF
from PIL import Image
import os
from re import split
from glob import glob

natsort = lambda s: [int(t) if t.isdigit() else t.lower() for t in split(r'(\d+)', s)]

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
        zoom = dpi / 72  # dpi scaling factor
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)

        # Convert the pixmap to an image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Save the image as a JPEG file
        output_path = os.path.join(output_folder, f"page_{page_number + 1}.jpg")
        img.save(output_path, "JPEG", quality=95)
        print(f"Saved {output_path}")

def rgb_to_cmyk_custom(image_path, output_path):
    # Open the image
    rgb_image = Image.open(image_path)
    rgb_image = rgb_image.convert("RGB")

    # Get image data
    pixels = rgb_image.getdata()
    cmyk_pixels = []

    for pixel in pixels:
        r, g, b = [x / 255.0 for x in pixel]

        # Convert RGB to CMY
        c = 1 - r
        m = 1 - g
        y = 1 - b

        # Convert CMY to CMYK
        k = min(c, m, y)
        if k == 1.0:
            c, m, y = 0, 0, 0
        else:
            c = (c - k) / (1 - k)
            m = (m - k) / (1 - k)
            y = (y - k) / (1 - k)

        # Convert to 8-bit values
        c = int(c * 255)
        m = int(m * 255)
        y = int(y * 255)
        k = int(k * 255)

        cmyk_pixels.append((c, m, y, k))

    # Create CMYK image
    cmyk_image = Image.new("CMYK", rgb_image.size)
    cmyk_image.putdata(cmyk_pixels)

    # Save CMYK image
    cmyk_image.save(output_path)
    print(f"Custom converted image saved to {output_path}")


def jpgs_to_pdf(jpg_list, output_pdf):
    """
    Convert a list of JPEG images to a single PDF.
    
    :param jpg_list: List of paths to JPEG images.
    :param output_pdf: Path to the output PDF file.
    """
    # Ensure the list is not empty
    if not jpg_list:
        print("The list of JPEGs is empty.")
        return

    # Open the first image and convert to RGB (necessary for PDF)
    image1 = Image.open(jpg_list[0]).convert('RGB')

    # Open the rest of the images and convert to RGB
    images = [Image.open(jpg).convert('RGB') for jpg in jpg_list[1:]]

    # Save all images to a single PDF
    image1.save(output_pdf, save_all=True, append_images=images)
    print(f"PDF saved to {output_pdf}")

if __name__ == "__main__":
    # Disassemble pdf to jpg, 
    pdf_list = sorted(glob('./to_convert_rgb_pdf/*'), key=natsort)
    pdf_len = len(pdf_list)
    print('Master Isei, the system is starting up.')
    for pdf_number in range(pdf_len):
        print(f'Processing the first pdf. PDF file: {pdf_list[pdf_number]}')

        pdf_to_jpegs_target_dir = f'./output_images/{pdf_number}_rgb_imgs'
        os.mkdir(pdf_to_jpegs_target_dir)

        pdf_to_jpegs(pdf_list[pdf_number], pdf_to_jpegs_target_dir, dpi=600)
        
        # Convert all jpg form rgb to cmyk
        jpg_list = sorted(glob(f'{pdf_to_jpegs_target_dir}/*'), key=natsort)
        cmyk_img_dir = f'./cmyk_jpg_out/{pdf_number}_cmyk_imgs'
        os.mkdir(cmyk_img_dir)

        # cmyk_out_dir = f'./cmyk_jpg_out/{pdf_number}'
        # os.mkdir(cmyk_out_dir)
        for i in range(len(jpg_list)):
            rgb_to_cmyk_custom(jpg_list[i], f'{cmyk_img_dir}/{i}.jpg')

        # Combine jpgs to pdf and sotre to ./converted_cmyk_pdf
        cmyk_jpg_list = sorted(glob(f'{cmyk_img_dir}/*'), key=natsort)
        pdf_target_path = f'./converted_cmyk_pdf/{pdf_number}_cmyk.pdf'
        jpgs_to_pdf(cmyk_jpg_list, pdf_target_path)

    # Clear cache
    os.system('rm -rf ./output_images/*')
    os.system('rm -rf ./cmyk_jpg_out/*')

    print('Master Isei, the calculations are finished.')