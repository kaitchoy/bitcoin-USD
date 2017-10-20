# bitcoin USD price 
import requests
from BeautifulSoup import BeautifulSoup
import json

url = 'https://api.coindesk.com/v1/bpi/currentprice/USD.json'
response = requests.get(url)
html = response.content
print "Bitcoin USD: " + html[397:405]

"""
html = response.content
print html


soup = BeautifulSoup(html)


title = soup.find('h1')
print title.text

price = soup.find('span', attrs={'class': 'data'})
print price.text.replace('-', '')
"""
