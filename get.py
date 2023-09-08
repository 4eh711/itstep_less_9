import urllib.request
import requests

opener = urllib.request.build_opener()
response = opener.open("https://itstep.org")
print(response.read())

response=requests.get("https://itstep.org")
print(response.content)
