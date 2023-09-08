import requests
from bs4 import BeautifulSoup

url = 'https://bank.gov.ua/'
response = requests.get(url)


if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')


    currency_block = soup.find('div', class_='value')


    usd_row = currency_block.find('td', text='USD')


    usd_rate = usd_row.find_next('td').text


    print('Usd_curse', usd_rate)
else:
    print('Error_to_open_page', response.status_code)



