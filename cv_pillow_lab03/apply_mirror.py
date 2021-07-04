# mirror : 좌우를 바꾸어 주는것
from PIL import Image, ImageOps

def mirror(image_path, output_path):
    image = Image.open(image_path)
    mirror_image = ImageOps.mirror(image)
    mirror_image.save(output_path)

if __name__ == "__main__":
    mirror("hummingbird.jpg", "hm_mirrored.jpg")