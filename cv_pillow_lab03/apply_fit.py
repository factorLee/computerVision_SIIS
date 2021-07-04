# fit() : crop()과 scale()이 합쳐진 것.
from PIL import Image, ImageOps

def fit(image_path, output_path, size, centering=(0.5,0.5)):
    image = Image.open(image_path)
    fit_image = ImageOps.fit(image, size, centering=centering)
    fit_image.save(output_path)

if __name__ == "__main__":
    fit("hummingbird.jpg", "hm_fit.jpg", size=(400,400))