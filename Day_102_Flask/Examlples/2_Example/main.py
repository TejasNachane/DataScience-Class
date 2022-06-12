from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route('/')
def Hello_World():
    return render_template('main.html')


@app.route('/hello<name>')
def my_function(name):
    return "Hello %s..!, Welcome to the Python Flask Framework...!!" %name


if __name__ == "__main__":
    app.run(debug=True)
