from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enter_new')
def new_employee():
    return render_template('Employee.html')


@app.route('/emp_details', methods=['POST', 'GET'])
def emp_details():
    if request.method == 'POST':
        try:
            emp_name = request.form['emp_name']
            emp_post = request.form['emp_post']
            emp_mobile = request.form['emp_mobile']
            emp_loc = request.form['emp_loc']
            emp_sal = request.form['emp_sal']

            with sql.connect('database.db') as con:
                cur = con.cursor()
                cur.execute('INSERT INTO Employee(emp_name, emp_post, emp_mobile, emp_loc,emp_sal)VALUES(?,?,?,?,?)',
                            (emp_name, emp_post, emp_mobile, emp_loc, emp_sal))
                con.commit()
                msg = 'Record added Successfully...!!'
        except:
            con.rollback()
            msg = 'Error in insert Operation...!!'
        finally:
            return render_template('result.html', msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect('database.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute('SELECT * FROM Employee')

    rows = cur.fetchall()
    return render_template('list.html', rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
