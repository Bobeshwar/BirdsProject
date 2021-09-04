from flask import Flask, request, jsonify, render_template, url_for
import tensorflow.keras as keras
import tensorflow
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from matplotlib import pyplot as plt
import numpy as np
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/predict_api', methods=["GET","POST"])
def list_post():
    json_body = request.get_json()
    predictions = 2 * json_body[0]   
    predictions = list(predictions)
    return jsonify(results = predictions)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)