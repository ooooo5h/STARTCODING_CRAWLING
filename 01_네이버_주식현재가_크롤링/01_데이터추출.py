import requests
from bs4 import BeautifulSoup

# 종목 코드 리스트
codes = [
    '095610',
    '006360',
    '114090',    
]

for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',', '')  # 문자열을 숫자로 바꾸기 위해서 ,를 제거해줌
    print(price) 