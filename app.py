
from flask import Flask
app = Flask(__name__)
print("hellow World");
@app.route('/')
def hello_world():
    return 'Hello Sammy!'

