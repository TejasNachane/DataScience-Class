import sqlite3 as sql

conn = sql.connect('database.db')
print('Open database Successfully...!')

conn.execute('CREATE TABLE Employee(emp_name TEXT, emp_post TEXT, emp_mobile TEXT, emp_loc TEXT, emp_sal TEXT)')
print('Table created Successfully...!')
conn.close()