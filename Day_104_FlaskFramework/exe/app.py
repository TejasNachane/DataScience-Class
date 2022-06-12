from argparse import _FormatterClass
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///students.sqlite3"
app.config['SECRET_KEY'] = "random strings"

db = SQLAlchemy(app)


class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    mobile = db.Column(db.String(10))

    def __init__(self, name, city, mobile):
        self.name = name
        self.city = city
        self.mobile = mobile


@app.route('/')
def home():
    return render_template('home.html' students=students.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == "POST":
        stud = students(
            request.form['name'], request.form['city'], request.form['mobile'])

        db.session.add(stud)
        db.session.commit()
        flash("Record added Successfully...!")
        return redirect(url_for('home'))
    return render_template('new.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000)
