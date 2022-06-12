from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__, template_folder='templates')

# conn = sql.connect('database.db')
# print("Database Created Successfully...!!")
#
# conn.execute('CREATE TABLE Employee(emp_name TEXT, emp_post TEXT, emp_mobile TEXT, emp_loc TEXT, emp_sal TEXT)')
# print("Table created Successfully...!!")
# conn.close()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enter_new')
def new_Employee():
    return render_template('employee.html')


@app.route('/')
def list():
    return render_template('list.html')


if __name__ == "__main__":
    app.run()
