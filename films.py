import requests
from bs4 import BeautifulSoup
import sys
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://thepage.ua/ua/news/10-novih-filmiv-2023-roku-sho-podivitisya-na-vihidnih'

response = requests.get(url)

if response.status_code == 200:
    bs = BeautifulSoup(response.text, features="html.parser")
    #print(bs)

    films = bs.find_all('h2')[:10]
    for i in films:
        print(i.text)