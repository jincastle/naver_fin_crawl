from bs4 import BeautifulSoup

f = open("01_h1_tage.html")

bsobj = BeautifulSoup(f, "html.parser")

h1 = bsobj.find('h1').text
p  = bsobj.find('p').text
ul = bsobj.find_all('ul')
print(h1)
print(p)
print(ul)