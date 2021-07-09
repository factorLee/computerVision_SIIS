import pyqrcode

msg = input("QR 코드로 변환할 메세지를 영어로 입력해주세요:")
qrcode = pyqrcode.create(msg)
qrcode.png("my_qrcode5.png", scale=5)
qrcode.png("my_qrcode10.png", scale=10)
print("QR 코드가 성공적으로 생성 되었습니다.")