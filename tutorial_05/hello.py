from flask import Flask
from markupsafe import escape
from flask import abort, redirect, url_for
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route("/")
def index():
    return "<p>I'm the index page!</p>"

@app.route("/<name>")
def hello_name(name):
    return f"Hello, {escape(name)}!"

@app.route('/hello')
def hello_world():
    return 'Hello, World'

@app.route('/file')
def file_01():
    return 'You accessed /file'

@app.route('/file/')
def file_02():
    return 'You accessed /file/'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

print('diagnostics')

@app.route('/login')
def login():
    abort(401)
    # this_is_never_executed()
