from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__, template_folder='templates')



@app.route('/result')
def result():
    my_dict = {'Physics': 84, 'Chemistry': 90, 'Biology': 86}
    return render_template('result.html', result=my_dict)


if __name__ == "__main__":
    app.run(debug=True, port=5053)
