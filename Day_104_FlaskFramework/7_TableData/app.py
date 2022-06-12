from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('employee.html')


@app.route('/result', methods =['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result =result)


if __name__ == "__main__":
    app.run(debug=True, port=5053)
