from bs4 import BeautifulSoup

bsobj = BeautifulSoup("<html><body><h1>안녕</h1></body></html>", "html.parser")
print(bsobj)

h1 = bsobj.find("h1")
print(h1)       # <h1>안녕</h1>
print(h1.text)  # 안녕

# .find()