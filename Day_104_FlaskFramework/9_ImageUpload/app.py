from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
app = Flask(__name__, template_folder='templates')


@app.route('/upload')
def index():
    return render_template('upload.html')


@app.route('/uploader', methods = ['POST','GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "File Upload Successfully"


if __name__ == "__main__":
    app.run(port=8084)
