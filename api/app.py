from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route('/get-random-number')
def get_random_number():
    return(jsonify({'number': int(random.random() * 1000000)}))
