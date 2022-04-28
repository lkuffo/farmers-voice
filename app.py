from dotenv import load_dotenv
from flask import Flask, render_template, make_response, request, send_file
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = './announcements'

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


@app.route('/announcements/<lang>/<filename>', methods=['GET'])
def play_announcement(lang, filename):
    path_to_file = "./announcements/" + lang + '/' + filename

    return send_file(
        path_to_file,
        mimetype="audio/wav",
        as_attachment=False)


@app.route('/play_announcements/<lang>', methods=['GET'])
def play_announcements(lang):
    file_endpoints = []
    for file in os.listdir('./announcements/' + lang):
        if file.endswith('.wav'):
            file_endpoints.append('/announcements/' + lang + '/' + file)
    print(file_endpoints)

    template = render_template('play_announcements.html', announcements=file_endpoints)
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response


@app.route('/announcement/<lang>', methods=['POST'])
def upload_voice(lang):
    # check if the post request has the file part
    print(request)
    print(request.files)
    if 'announcement' not in request.files:
        return 'not good', 500
    file = request.files['announcement']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], lang, filename))
    template = render_template('announcement_saved.html')
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response


if __name__ == "__main__":
    app.run(debug=True, port=8081, host='0.0.0.0')

