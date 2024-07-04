from PIL import Image
import os
from datetime import datetime


def resize_images_in_folder(input_folder, output_folder, size):
    """Resize all images in the specified folder and save them to the output folder.

    Args:
        input_folder (str): Path to the input folder containing images.
        output_folder (str): Path to the output folder to save resized images.
        size (tuple): Desired size (width, height).
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        if os.path.isfile(input_path):
            try:
                with Image.open(input_path) as img:
                    img = img.resize(size)
                    img.save(output_path)
                    print(f"Resized image saved to {output_path}")
            except Exception as e:
                print(f"Failed to resize {input_path}: {e}")


if __name__ == "__main__":
    input_folder = 'input_images'

    # Create the output folder path with the current date
    date_str = datetime.now().strftime("%d%m%Y")
    output_folder = os.path.join(os.path.expanduser("~"), "Pictures", "PyResizer", date_str)

    size = (128, 128)  # Desired size (width, height)

    resize_images_in_folder(input_folder, output_folder, size)
