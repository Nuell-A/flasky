from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, world</h1>'

@app.route('/user/<name>')
def user(name):
    # 'format(name)' is inserted in place of the curly braces
    return '<h1>Hello, {}</h1>'.format(name)
    
