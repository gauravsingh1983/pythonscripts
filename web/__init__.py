#!flask/bin/python
from flask import Flask, jsonify, request, json
import requests
import time
from core import test_class
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


tasks = [
    {
        'Approve': 72,
        'Spam': 18.5,
        'Hate Speech': 2.3, 
        'Far Right': 0,
        'Harassment' : 7.2
    }
]

@app.route('/pace/predict', methods=['GET'])
def get_pace_data():
    return jsonify(tasks)


@app.route('/pace/message', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    else:
        return "415 Unsupported Media Type ;)"
    

@app.route('/test', methods=['GET'])
def get_test():
    f = test_class.Fridge()
    return jsonify(f.in_fridge('apples'))


if __name__ == '__main__':
    app.run(port=5001, debug=True)