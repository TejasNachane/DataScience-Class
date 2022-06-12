from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/success/<name>')
def success(name):
    return 'Hello %s..!, Welcome to Python and Data Science Placement Batch ' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user))


if __name__ == "__main__":
    app.run(debug=True, port=5053)
