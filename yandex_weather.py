from bs4 import BeautifulSoup
import requests
response = requests.get("https://meteofor.com.ua/ru/weather-kremenchuk-4968/now/")
print(response)

