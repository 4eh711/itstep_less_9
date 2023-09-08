import requests

response = requests.get("https://cryptorank.io/")
response_text = response.text
response_parse = response_text.split("<p>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        print(parse_elem_1)