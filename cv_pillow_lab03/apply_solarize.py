# 
from PIL import Image, ImageOps

def solarize(image_path, output_path, threshold=128):
    image = Image.open(image_path)
    solarize_image = ImageOps.solarize(image, threshold=threshold)
    solarize_image.save(output_path)

if __name__ == "__main__":
    solarize("hummingbird.jpg", "hm_solarize.jpg")
    