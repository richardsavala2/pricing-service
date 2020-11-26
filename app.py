import requests
from bs4 import BeautifulSoup

URL = "https://www.johnlewis.com/2020-apple-ipad-pro-11-inch-a12z-bionic-ios-wi-fi-128gb/space-grey/p4949052"
TAG_NAME = "p"
QUERY = {"class": "price price--large"}

response = requests.get(URL)
content = response.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find(TAG_NAME, QUERY)
string_price = element.text.strip()

print(string_price)
