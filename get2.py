import requests

response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for elem_1 in response_parse:
    if elem_1.startswith("$"):
        print(elem_1)