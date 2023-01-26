import requests
from bs4 import BeautifulSoup

def crawl(code):
    url = f'https://finance.naver.com/item/main.naver?code={code}'
    res = requests.get(url)
    bsobj = BeautifulSoup(res.text, 'html.parser')

    div_today = bsobj.find('div', {'class' : 'today'})
    em = div_today.find('em')
    price = em.find('span',{'class':'blind'}).text

    h_company = bsobj.find('div', {'class' : 'h_company'})
    name = h_company.a.text # <a>를 불러서 텍스트
    div_description = h_company.find('div', {'class':'description'})
    code = div_description.span.text

    table_no_info = bsobj.find('table', {'class':'no_info'})
    tds = table_no_info.tr.find_all('td') # <tr>안에 있는 <td> 전체를 불러온다
    volume = tds[2].find('span', {'class':'blind'}) # 리스트 형태로 나온거에서 3번째거

    dic = {"price": price,'name': name, 'code':code , 'volume':volume}
    return dic

if __name__ == '__main__':
    dic = crawl('035720')
    print(dic)