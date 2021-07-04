# watermark 처리를 할 때 transparency를 지원하지 않는 이미지면 에러 발생
# 다시하기

from PIL import Image

def watermark_with_transparency(input_image_path, output_image_path, watermark_image_path, position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size
    transparent = Image.new("RGB", (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.save(output_image_path)
    
if __name__ == "__main__":
    watermark_with_transparency("hummingbird.jpg", "hummingbird_watermarked_2.jpg", "logo.png", position=(10,10))

