
from PIL import Image, ImageOps

def invert(image_path, output_path):
    image = Image.open(image_path)
    invert_image = ImageOps.invert(image)
    invert_image.save(output_path)

if __name__ == "__main__":
    invert("hummingbird.jpg", "hm_inverted.jpg")