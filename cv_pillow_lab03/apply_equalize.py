# histogram
from PIL import Image, ImageOps

def equalize(image_path, output_path):
    image = Image.open(image_path)
    equalize_image = ImageOps.equalize(image)
    equalize_image.save(output_path)

if __name__ == "__main__":
    equalize("hummingbird.jpg", "equalize.jpg",)