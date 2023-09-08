import requests
from bs4 import BeautifulSoup

url ='https://bank.gov.ua/'
response = requests.get(url)

if response.status_code == 200:
    #soup = BeautifulSoup(response.text, 'html.parser')
    bs = BeautifulSoup(response.text, 'html.parser')
    #print(bs)
    temp = bs.find('div', {"class":"value-full"})
    print(temp.text)
    #soup_list = soup.find_all("div", {"class":"value-full"})
    #usd_rate = soup_list[0].find("div")
    #print(usd_rate)
#else:
  #  print(response.status_code)
    #soup_list = soup.find_all("div", {"class": "value-full"})

    #for elem in soup_list:

        #if elem.text.strip():
            #print(elem.text.strip())

