from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route('/')
def Hello_World():
    return render_template('main.html')


@app.route('/hello')
def my_function():
    return "Welcome to the Flask Framework...!!"


if __name__ == "__main__":
    app.run(debug=True)
