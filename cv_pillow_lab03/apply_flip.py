
from PIL import Image, ImageOps

def flip(image_path, output_path):
    image = Image.open(image_path)
    flip_image = ImageOps.flip(image)
    flip_image.save(output_path)

if __name__ == "__main__":
    flip("hummingbird.jpg", "hm_flip.jpg")