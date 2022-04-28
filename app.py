from dotenv import load_dotenv
from flask import Flask, render_template, make_response, request
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/announcements'

load_dotenv()
app = Flask('app')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

####################
# ENDPOINTS
####################


@app.route('/vxml', methods=['GET'])
def vxml():
    template = render_template('main.html')
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response


@app.route('/announcement', methods=['POST'])
def upload_voice():
    # check if the post request has the file part
    if 'file' not in request.files:
        return 'not good', 500
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'ok', 200


if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')

