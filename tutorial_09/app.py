import datetime
from flask import Flask, render_template
from jinja2 import StrictUndefined
from wtforms import Form, BooleanField, StringField, validators, PasswordField

app = Flask(__name__)

app.jinja_env.undefined = StrictUndefined
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


class LoginForm(Form):
  username = StringField('Username')
  password = PasswordField('Password')


form = LoginForm()


@app.route('/')
def index():
  return render_template('index.html',
                         utc_dt=datetime.datetime.utcnow(),
                         form=form
                         )


@app.route('/about/')
def about():
  return render_template('about.html',
                         utc_dt=datetime.datetime.utcnow(),
                         )
