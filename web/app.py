#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run()