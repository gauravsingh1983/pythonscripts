#!flask/bin/python
from flask import Flask, jsonify, request
import requests
import time
from BeautifulSoup import BeautifulSoup

app = Flask(__name__)

@app.route('/ytc/search', methods=['GET'])
def get_tasks():
    start_time = time.time()
    q1 = request.args.get('q')
    url = 'https://www.google.co.in/search?q='+q1
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
    div = soup.find('div', attrs={'id': 'res'})
    jsonArr = []
    for row in div.findAll('cite'):
        jsonArr.append(row.text)  
        
    jsonArr =  [k for k in jsonArr if 'wikipedia' in k]
    print("--- %s seconds ---" % (time.time() - start_time))       
    return jsonify({'links': jsonArr})


@app.route('/ytc/redosearch', methods=['GET'])
def get_tasks_redo():
    w = 'wiki'
    yt = 'youtuber'
    start_time = time.time()
    q1 = request.args.get('q')
    jsonArr = []       
    url = 'https://www.google.co.in/search?q='+q1+w
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
    div = soup.find('div', attrs={'id': 'res'})
    for row in div.findAll('cite'):
        jsonArr.append(row.text) 
        
    url = 'https://www.google.co.in/search?q='+q1+yt
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
    div = soup.find('div', attrs={'id': 'res'})
    for row in div.findAll('cite'):
        jsonArr.append(row.text)
    
    jsonArr =  [k for k in jsonArr if 'wikipedia' in k]  
    print("--- %s seconds ---" % (time.time() - start_time))       
    return jsonify({'links': jsonArr})

if __name__ == '__main__':
    app.run(port=5001)