from flask import Flask

app = Flask(__name__)


@app.route('/flask')
def hello_flask():
    return 'Welcome to Flask Framework...!'


@app.route('/python')
def hello_python():
    return 'Welcome to Python Programming'


if __name__ == "__main__":
    app.run(debug=True, port=5002)
