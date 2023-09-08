import requests

res = requests.get("https://itstep.org/")

print(res.text)