
from PIL import Image, ImageOps

def posterize(image_path, output_path, bits):
    image = Image.open(image_path)
    posterize_image = ImageOps.posterize(image, bits=bits)
    posterize_image.save(output_path)

if __name__ == "__main__":
    posterize("hummingbird.jpg", "hm_posterize.jpg", bits=2) # bits= 1~8
    