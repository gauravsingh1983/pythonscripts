import requests
URL = 'https://www.google.co.in'
proxy = {'http': 'http://www.google.co.in'}
r = requests.get(URL, proxies = proxy)
print r.text