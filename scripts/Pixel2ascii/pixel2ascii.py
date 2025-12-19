import os
from PIL import Image
import argparse

# ASCII characters used to represent pixel intensity (from dark to light)
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    """Resize the image to maintain aspect ratio."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.5)  # Adjust for terminal character height
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    """Convert image to grayscale."""
    return image.convert("L")

def pixels_to_ascii(image):
    """Convert pixel brightness to ASCII characters."""
    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel // 25] for pixel in pixels)  # Map brightness levels to ASCII
    return ascii_str

def convert_image_to_ascii(image_path, output_width=100, save_to_file=None):
    """Convert a single image to ASCII."""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error: Unable to open image {image_path}. {e}")
        return

    image = resize_image(image, output_width)
    image = grayscale_image(image)
    ascii_str = pixels_to_ascii(image)

    # Format ASCII string to match image dimensions
    ascii_str = "\n".join(
        ascii_str[i : i + image.width] for i in range(0, len(ascii_str), image.width)
    )

    if save_to_file:
        with open(save_to_file, "w") as f:
            f.write(ascii_str)
        print(f"ASCII art saved to {save_to_file}")
    else:
        print(ascii_str)

def batch_convert_images(image_paths, output_dir, width=100):
    """Process multiple images and save ASCII output to text files."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for image_path in image_paths:
        filename = os.path.basename(image_path)
        output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
        convert_image_to_ascii(image_path, width, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images to ASCII art.")
    parser.add_argument("-f", "--folder", help="Path to a folder containing images")
    parser.add_argument("-i", "--images", nargs="+", help="List of specific image files")
    parser.add_argument("-w", "--width", type=int, default=100, help="Output width of ASCII art")
    parser.add_argument("-o", "--output", default="ascii_output", help="Output folder for ASCII files")

    args = parser.parse_args()

    if args.folder:
        # Process all images in the folder
        supported_formats = (".png", ".jpg", ".jpeg", ".bmp", ".gif")
        image_paths = [
            os.path.join(args.folder, f) for f in os.listdir(args.folder) if f.lower().endswith(supported_formats)
        ]
        batch_convert_images(image_paths, args.output, args.width)

    elif args.images:
        # Process specific images
        batch_convert_images(args.images, args.output, args.width)

    else:
        print("Error: You must specify either a folder (-f) or a list of images (-i).")
