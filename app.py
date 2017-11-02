#!flask/bin/python
from flask import Flask, jsonify, request
import requests 
from BeautifulSoup import BeautifulSoup

app = Flask(__name__)

@app.route('/ytc/search', methods=['GET'])
def get_tasks():
	q1 = request.args.get('q')
	url = 'https://www.google.co.in/search?q='+q1
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html)
	div = soup.find('div', attrs={'id': 'res'})
	jsonArr = []
	for row in div.findAll('cite'):
		jsonArr.append(row.text)	
			
	return jsonify({'links': jsonArr})

if __name__ == '__main__':
    app.run(port=5001)