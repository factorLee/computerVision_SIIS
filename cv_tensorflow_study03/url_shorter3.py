import pyshorteners

url = input("줄이고자 하는 Url을 입력해주세요 :")
short_url = pyshorteners.Shortener().tinyurl.short(url)

print("줄여진 URL :", short_url)
