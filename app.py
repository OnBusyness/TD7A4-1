from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("db", 27017)
db = client["mydatabase"]
collection = db["mycollection"]

@app.route("/")
def index():
    with open('data/message.txt', 'r') as f:
        message = f.read()
    return f'<h1>{message}</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
