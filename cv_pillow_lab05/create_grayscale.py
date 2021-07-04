# 2. 색바꾸기 
from PIL import Image

def grayscale(input_image_path, output_image_path):
    color_image = Image.open(input_image_path)
    gray_scale = color_image.convert("L")
    # gray_scale = color_image.convert("1") # 블랙앤화이트
    # gray_scale = color_image.convert("1", dither=0) #
    gray_scale.save(output_image_path)

if __name__ == "__main__":
    grayscale("monarch_caterpillar.jpg", "bw_caterpillar.jpg")