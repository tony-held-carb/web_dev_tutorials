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
    # Using formating string
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/capitalize2/<word>/')
def capitalize2(word):
    # Using f string
    return f"<h1>{escape(word.capitalize())}</h1>"

@app.route('/add_me/<var_1>/<var_2>')
def add_me(var_1, var_2):
    # Using f string
    return f"<h1>The sum of {var_1} and {var_2} is {int(var_1)+int(var_2)}</h1>"

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)