# Image classification of flowers using pretrained CNN models
Developing and productization of a Machine Learning model for Classification of 5 Types of flowers.  
Deployed to hugging face spaces for interactivity and great UI.   

### Dataset description
https://www.kaggle.com/datasets/alxmamaev/flowers-recognition

## Context
This dataset contains 4242 images of flowers.
The data collection is based on the data flicr, google images, yandex images.
You can use this datastet to recognize plants from the photo.

## Content
The pictures are divided into five classes: daisy, dandelion, rose, sunflower, tulip.
For each class there are about 800 photos. Photos are not high resolution, about 320x240 pixels. Photos are not reduced to a single size, they have different proportions!

## Inspiration

What kind of flower is that?

### Technologies
- Python
- Tensorflow / Tensorflow Lite  
- Keras  
- Models: Desnet201, EfficientNetV2S, Resnet50
- Numpy, Pandas, MatplotLib
- Flask and Gradio 
- Hugging Face Spaces
- Docker
- AWS EC2    
- Pytest  

[HUGGINGFACE SPACES.webm](https://user-images.githubusercontent.com/21258579/209125240-41d719bb-99c7-4d2c-94ca-5ce0c5f6655a.webm)

### Development Plan: 
- Setup environment
- Download Dataset
- Development -> notebook.ipynb, train.py, convert_model.py
  - Visualize images
  - Prepare dataset: train-val-test split
  - Create model Xception (imagenet coefs)
	- Add checkpoints
	- Select learning rate
	- Add inner layers
	- Add dropout regularization
	- Perform data augmentation
	- Train with larget files (299x299)
	- Test the model with test set
	- Train efficient-net-b2 for comparison
  - Final model trainning script using the full_train and test datasets
  - Model conversion to tf_lite
- Productization -> ./production/*
  - Create tf-serving image
  - Create gateway (FastAPI) image
  - Create tests for testing the images (with docker-compose)
  - Create Kubernetes yaml files (kind and EKS)
    - gateway service and deployment
    - tf-serving service and deployment
  - Create Streamlit app
  - Performance test with Locust
- Documentation



