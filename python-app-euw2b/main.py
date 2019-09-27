from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route('/api/get-random-number')
def get_random_number():
    return(jsonify({'number': int(random.random() * 1000000)}))


@app.route('/')
def get_number_page():
    return(f"<h1> {int(random.random() * 1000000)}")

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
