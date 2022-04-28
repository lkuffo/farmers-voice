from dotenv import load_dotenv
from flask import Flask, render_template, make_response

load_dotenv()
app = Flask('app')

####################
# ENDPOINTS
####################


@app.route('/vxml', methods=['GET'])
def vxml():
    template = render_template('main.html')
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response


if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')

