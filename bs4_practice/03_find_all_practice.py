from bs4 import BeautifulSoup

f = open("ul_li.html", encoding='utf-8')

bsobj = BeautifulSoup(f.read(), 'html.parser')

ul = bsobj.find('ul')
li = ul.find('li') # 1개만 나옴
lis = ul.find_all('li')
print(lis) # 리스트 형태로 나옴
for i in lis:
    print(i.text)

li_all = bsobj.find_all('li') # 전체 그래서 자세히 뽑을려면 ul을 걸쳐서 뽑는게 좋다
for i in li_all:
    print(i.text)
