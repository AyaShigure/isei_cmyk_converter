from PIL import Image
from re import split
from glob import glob

natsort = lambda s: [int(t) if t.isdigit() else t.lower() for t in split(r'(\d+)', s)]

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

if __name__ == "__main__":
    pics_list = sorted(glob('./output_images/*'), key=natsort)
    for i in range(len(pics_list)):
        rgb_to_cmyk_custom(pics_list[i], './converted_out/{}.jpg'.format(i))
