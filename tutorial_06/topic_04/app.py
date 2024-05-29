from flask import Flask, render_template, request, url_for, flash, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is an unsecure secret key for dev purposes'

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]



@app.route('/')
def index():
    return render_template('index.html', messages=messages)

# @app.route('/create/', methods=('GET', 'POST'))
# def create():
#   if request.method == 'POST':
#     print(f"method is post")
#   print(f"{request.form=}")
#   return render_template('create.html')

@app.route('/create/', methods=('GET', 'POST'))
def create():
  print(f"{request.form=}")
  if request.method == 'POST':
      title = request.form['title']
      content = request.form['content']

      if not title:
        msg = 'Title is required!'
        print(msg)
        flash(msg)
      elif not content:
        msg = 'Content is required!'
        print(msg)
        flash(msg)
      else:
          messages.append({'title': title, 'content': content})
          return redirect(url_for('index'))

  return render_template('create.html')
