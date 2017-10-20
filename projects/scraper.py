# bitcoin USD price 
import requests
from BeautifulSoup import BeautifulSoup
import json

url = 'https://api.coindesk.com/v1/bpi/currentprice/USD.json'
html = requests.get(url).content
bt = json.loads(str(html))
print "Bitcoin in USD: $" + bt["bpi"]["USD"]["rate"]
