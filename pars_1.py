from bs4 import BeautifulSoup
import requests
response = requests.get("https://coinmarketcap.com/")
print(response)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    list = soup.find_all("a", {"href": "/currencies/bitcoin/#markets"})
    res = list[0].find("span")
    print(res.text)

