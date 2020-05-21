import flask
import os
from config import *

from flask import url_for
from werkzeug.utils import secure_filename

from queryHandler import *
configuration=get_config()
UPLOAD_FOLDER = configuration["UPLOAD_FOLDER"]
print(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = flask.Flask(__name__)

app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/pageinfo', methods=['POST'])
def create_task():
    #img_path = "C:\\Users\\maitreyee\\Documents\\Shikhya\\Code\\BookScanService\\images1\\3\\IMG_20200112_104638.jpg"
    if 'file' not in flask.request.files:
        flask.flash('No file part')
        return flask.redirect(flask.request.url)
    file = flask.request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flask.flash('No selected file')
        #return flask.redirect(flask.request.url)
    if file and allowed_file(file.filename):
        print(file.filename)
        filename = secure_filename(file.filename)
        img_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(img_path)
        #return flask.redirect(url_for('uploaded_file',
        #                              filename=filename))
    page_info = checkPageInfo(img_path)
    return flask.jsonify({'pagenumber': page_info}), 201


@app.route('/', methods=['GET'])
def index():
    return flask.render_template("index.html")

app.run()
