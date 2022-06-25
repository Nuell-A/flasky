from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    # 'format(name)' is inserted in place of the curly braces
    return render_template('user.html',  name=name)
    
