import requests
from BeautifulSoup import BeautifulSoup

url = 'https://www.google.co.in/search?q=aronra'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
div = soup.find('div', attrs={'id': 'res'})
for row in div.findAll('cite'):
    print row.text
