import os
from flask import Flask, request, redirect, url_for
from flask import render_template

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
ALLOWED_EXTENSIONS = set(['yml'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

from views import *

if __name__ == '__main__':
    app.run(debug=True)