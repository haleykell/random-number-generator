from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route('/api/get-random-number')
def get_random_number():
    return(jsonify({'number': int(random.random() * 1000000)}))


@app.route('/')
def get_number_page():
    return(f"<h1> {int(random.random() * 1000000)}")
