"""Scripts to add data to the sql database using sqlalchemy."""

from app import app, db, Student


def create_tables():
  db.create_all()


def student_diag(student):
  print(f"Student Diagnostics for: {student}")
  print(f"{student.id=}")
  print(f"{student.firstname=}")
  print(f"{student.lastname=}")
  print(f"{student.email=}")
  print(f"{student.age=}")
  print(f"{student.bio=}")


def populate_tables():
  john = Student(firstname='john', lastname='doe',
                 email='jd@example.com', age=23,
                 bio='Biology student')
  student_diag(john)

  sammy = Student(firstname='Sammy',
                  lastname='Shark',
                  email='sammyshark@example.com',
                  age=20,
                  bio='Marine biology student')
  student_diag(sammy)

  carl = Student(firstname='Carl',
                 lastname='White',
                 email='carlwhite@example.com',
                 age=22,
                 bio='Marine geology student')
  student_diag(carl)

  db.session.add(john)
  db.session.add(sammy)
  db.session.add(carl)
  db.session.commit()


def query_students():
  students = Student.query.all()
  print(f"{students=}")


if __name__ == '__main__':
  with app.app_context():
    # create_tables()
    # populate_tables()
    query_students()
