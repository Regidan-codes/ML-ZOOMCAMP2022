!pip install gradio

import gradio as gr

from keras.models import load_model,Sequential

from google.colab import drive
drive.mount('/content/drive')

model = load_model("./Model_2.h5")

class_names = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

def predict_image(img):
  img_4d=img.reshape(-1,331,331,3)
  prediction=model.predict(img_4d)[0]
  return {class_names[i]: float(prediction[i]) for i in range(5)}

image = gr.inputs.Image(shape=(331,331))
label = gr.outputs.Label(num_top_classes=5)
gr.Interface(fn=predict_image, 
             inputs=image, 
             outputs=label, 
             interpretation='default', 
             title = 'Flower Recognition App', 
             description= 'Get probability for input image among 5 classes').launch(share=True)
