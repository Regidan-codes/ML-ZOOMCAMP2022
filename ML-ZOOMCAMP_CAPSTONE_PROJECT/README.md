# Image classification of flowers using pretrained CNN models
Development and deploying deep learning model for classification of 5 Types of flowers.  
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

[HUGGINGFACE SPACES.webm](https://user-images.githubusercontent.com/21258579/209125240-41d719bb-99c7-4d2c-94ca-5ce0c5f6655a.webm)

### Development Plan: 
- Setup environment
- Download Dataset
- Development -> notebook.ipynb, train.py
  - Visualize images
  - Prepare dataset: train-val-test split
  - Create model Desnet201 (imagenet coefs)
	- Add checkpoints
	- Select learning rate
	- Add inner layers
	- Add dropout regularization
	- Perform data augmentation
	- Train with larget files (331x331)
	- Test the model with test set
   - Create model EfficienetV2S (imagenet coefs)	
   - Create model Resnet50 (imagenet coefs)
   -Choose the best model among 3 model applications and save it as .h5 model
  - Final model training script using the full_train and test datasets
  - Model saved will be used in flask
- Production
  - Create gateway (Flask) image and Gradio
  - Create Dockerfile
  - Create AWS EC2 instance
  - Create Huggingface spaces app gradio web API
- Documentation

## Setup

Follow the instructions in [SETUP.md](./SETUP.md)  

### Clone the repo
Open a shell (e.g. Powershell) and execute:  
`https://github.com/Regidan-codes/ML-ZOOMCAMP2022.git`

### Download the dataset
Go to https://www.kaggle.com/datasets/alxmamaev/flowers-recognition 
Create a Kaggle account and click Download button.  
The zip file actually contains 5 datasets, each one in a subdirectories.   
So unzip the folder `Flower-Recognition` into the `data` folder of the repository.
...

### Create the environment

Open a shell (GitBash, bash or Powershell) and execute the following instructions:

Note:
If there is an error when starting Powershell and the conda base environment is not activated by default (you should see (base)), try with:  
`powershell -executionpolicy remotesigned`  
or in an already launched powershell: `set-executionpolicy remotesigned`  
To check the policy:  
`get-executionpolicy` (default is restricted)  
You may set the default execution policy at any time.

Create a conda environment (recommended):  
In the root directory of the repository, execute:  
`conda create --name py39 python=3.9`  
`conda activate py39`
Install pip
`pip install -U pip` alternatively `python.exe -m pip install -U pip`  

To create the development environment and install dependencies, download environment.yml:    

```

conda env create -n ENVNAME --file environment.yml

```


Please, note that the production/gateway and production/fron-end have their specific environments in order to keep these environments separated from the development environment and from each other.  

To check the tensorflow version and GPU devices used (if any):
`python`  
`import tensorflow as tf`  
`tf.config.list_physical_devices('GPU')`  
`[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]`  

## Development:

**jupyter notebook**  
 Ensure that the development environment is active, then start jupyter notebook with:
`jupyter notebook`  

Go the browser and open `notebook.ipynb`   
Run all cells check the tranning of models and model evaluation.
The best model is saved as `.h5` in the directory by using checkpoints, which called when the model accuracy improves for each epoch.  
 
Finally, the final model is trained with images of size of 331x331.   

The best model is selected and tested with the test dataset.
Finally, the best model is saved as .h5 file.  
 
Check the model using app.py or gradio.py which ever you're comfortable with

**Train script**  
The model with the best parameters will be trained by using the full_train dataset and checking its performance with the test_dataset.  
Is a shell with the development environment activated, run:  
`python train.py`  
The best checkpoint is automatically selected and the model is saved as .h5 file.  

## Production:

The application 'Flower-Recognition' is a hugginface spaces app that
- Ask the user to input any image from 5 classes mentioned
- Predicts the probablities of varieties by sending a request to the gateway
- Shows the probablities of all 5 classes in a cleaner UI

You can test the cloud web app - [CLICK-HERE](https://huggingface.co/spaces/regidancodes/gradio-Flower-recognition-App)
