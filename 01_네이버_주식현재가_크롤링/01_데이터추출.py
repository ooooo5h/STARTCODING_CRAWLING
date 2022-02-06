import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/sise.naver?code=000660"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
price = soup.select_one("#_nowVal").text
price = price.replace(',', '')  # 문자열을 숫자로 바꾸기 위해서 ,를 제거해줌
print(price)