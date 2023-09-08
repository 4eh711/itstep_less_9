from bs4 import BeautifulSoup
import requests

response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    list = soup.find_all("a", {"href": "/currencies/bitcoin/#markets"})
    for elem in list:
        print(elem.text)







