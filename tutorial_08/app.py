import datetime
from flask import Flask, render_template
from jinja2 import StrictUndefined

app = Flask(__name__)

app.jinja_env.globals.update(zip=zip)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.route('/')
def index():
    return render_template('index.html',
                           utc_dt=datetime.datetime.utcnow(),
                           )

@app.route('/macro_01/')
def macro_01():
    return render_template('macro_01.html',
                           utc_dt=datetime.datetime.utcnow(),
                           )
@app.route('/macro_02/')
def macro_02():
    return render_template('macro_02.html',
                           utc_dt=datetime.datetime.utcnow(),
                           )

@app.route('/macro_03/')
def macro_03():
    return render_template('macro_03.html',
                           utc_dt=datetime.datetime.utcnow(),
                           )

@app.route('/calls/')
def calls():
    return render_template('calls.html',
                           utc_dt=datetime.datetime.utcnow(),
                           )

@app.route('/filtering/')
def filtering():
    return render_template('filtering.html',
                           utc_dt=datetime.datetime.utcnow(),
                           )
