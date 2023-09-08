from bs4 import BeautifulSoup
import requests

url ='https://rb.gy/0ty80'
response = requests.get(url)
print(response)
if response.status_code==200:
  bs = BeautifulSoup(response.text, "html.parser")
  temp = bs.find("p","today-temp")
  print(temp.text)