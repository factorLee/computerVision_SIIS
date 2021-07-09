from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("my_qrcode10.png")

decoding_qr = decode(img)

print("QR 코드에 담겨진 내용은:")
print(decoding_qr[0].data.decode())