from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
from tensorflow import keras

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

#name classes 
classes = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = './models/Model_resnet.h5'

# Load your trained model
#model = load_model(MODEL_PATH)
#model._make_predict_function()          # Necessary
# print('Model loaded. Start serving...')

# You can also use pretrained model from Keras
# Check https://keras.io/applications/
from keras.applications.resnet import ResNet50
model = ResNet50(weights='imagenet')
model.save('resnet.h5')
print('Model loaded. Check http://127.0.0.1:5000/')


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    img_arr = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    img_arr_expnd  = np.expand_dims(img_arr,axis=0)
    img = keras.applications.resnet.preprocess_input(img_arr_expnd)  
    pred = model.predict(img)
    return pred


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)

        # Process your result for human
        # pred_class = preds.argmax(axis=-1)            # Simple argmax
        result = classes[np.argmax(preds)]               # Convert to string
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)