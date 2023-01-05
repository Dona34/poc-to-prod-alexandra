import flask
import io
import string
import time
import os
import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, request
from predict.predict.run import TextPredictionModel
#model load and cleaning
#model = tf.keras.models.load_model("model.h5")

app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def get_text():
    #text = request.args.get('text')
    model = TextPredictionModel.from_artefacts("")


    text =  "this is a python script"

    #print(TextPredictionModel.predict(text,3))

    predictions = model.predict([text])
    print(predictions)
    #return jsonify(model.predict(text))


@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Inference'


if __name__ == '__main__':
    app.run(debug=True)