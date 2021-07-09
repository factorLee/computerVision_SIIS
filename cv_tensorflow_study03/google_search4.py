from googlesearch import search
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
query = input("무엇을 검색하고 싶으신가요?")

for i in search(query, start=0, stop=10):
    print(i)