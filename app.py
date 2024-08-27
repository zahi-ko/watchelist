from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return r'<h1>Hello World!</h1>'