from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__, template_folder='templates')
app.secret_key = "random string"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = "Invalid Username or Password, Please try again later...!"
        else:
            flash("You were login Successfully...!")
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(port=8084)
