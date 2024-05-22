from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
@app.route('/main/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    return '<h2>Hi {}</h2>'.format(users[user_id])
