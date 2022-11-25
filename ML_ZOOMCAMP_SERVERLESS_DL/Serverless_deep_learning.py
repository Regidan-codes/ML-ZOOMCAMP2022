
import tflite_runtime.interpreter as tflite
import os
from io import BytesIO
from urllib import request
from PIL import Image
import numpy as np

MODEL_NAME = os.getenv('MODEL_NAME', 'dino-vs-dragon-v2.tflite')

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img


def process_input(x):
    return x/255


interpreter = tflite.Interpreter(model_path=MODEL_NAME)
interpreter.allocate_tensors()


input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']


def predict(url):
    img = download_image(url)
    img = prepare_image(img, target_size=(150, 150))

    a = np.array(img, dtype='float32')
    X = np.array([a])
    X = process_input(X)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    return float(preds[0, 0])

def lambda_handler(event, context):
    url = event['url']
    pred = predict(url)
    result = {
        'prediction' : pred
    }
    return result
