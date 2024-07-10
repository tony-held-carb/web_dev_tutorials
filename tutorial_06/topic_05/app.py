from flask import Flask, render_template, redirect, url_for
from forms import CourseForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

courses_list = [{
  'title': 'Python 101',
  'description': 'Learn Python basics',
  'price': 34,
  'available': True,
  'level': 'Beginner'
}]


def obj_diagnostics(obj, include_hidden=False, include_functions=False):
  for attr_name in dir(obj):
    attr_value = getattr(obj, attr_name)
    if not attr_name.startswith('_') or include_hidden:
      if callable(attr_value):
        if include_functions:
          print(f"{attr_name}(): is function")
      else:
        print(f"{attr_name} {type(attr_value)}:\n\t {attr_value}")


@app.route('/', methods=('GET', 'POST'))
def index():
  form = CourseForm()
  obj_diagnostics(form)

  print(f"{form.validate_on_submit()=}")
  if form.validate_on_submit():
    courses_list.append({'title': form.title.data,
                         'description': form.description.data,
                         'price': form.price.data,
                         'available': form.available.data,
                         'level': form.level.data
                         })
    return redirect(url_for('courses'))
  return render_template('index.html', form=form)

@app.route('/add_course/', methods=('GET', 'POST'))
def add_course():
  form = CourseForm()
  obj_diagnostics(form)

  print(f"{form.validate_on_submit()=}")
  if form.validate_on_submit():
    courses_list.append({'title': form.title.data,
                         'description': form.description.data,
                         'price': form.price.data,
                         'available': form.available.data,
                         'level': form.level.data
                         })
    return f"your course has been added"
  return render_template('add_course.html', form=form)

@app.route('/courses/')
def courses():
  return render_template('courses.html', courses_list=courses_list)
