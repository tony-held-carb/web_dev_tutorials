from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
@app.route('/main/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

@app.route('/capitalize1/<word>/')
def capitalize1(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/capitalize2/<word>/')
def capitalize2(word):
    return f"<h1>{escape(word.capitalize())}</h1>"
