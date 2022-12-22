import numpy as np

from tensorflow import keras
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator as imgen
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.callbacks import EarlyStopping,ModelCheckpoint

from sklearn.metrics import classification_report,confusion_matrix

from keras.applications.efficienet_v2 import EfficientNetV2S
print("Libraries Imported !!")


# Defining data augmentation

traingen = imgen(#rescale=1./255,
                 preprocessing_function = keras.applications.efficienet_v2.preprocess_input,
                 zoom_range=0.2,
                 shear_range=0.2,
                 vertical_flip=True,
                 horizontal_flip=True,
                 width_shift_range=0.2,
                 height_shift_range=0.2,
                 fill_mode="nearest"
                 )
valgen = imgen(#rescale=1./255,
preprocessing_function = keras.applications.efficienet_v2.preprocess_input,
                 zoom_range=0.2,
                 shear_range=0.2,
                 vertical_flip=True,
                 horizontal_flip=True,
                 width_shift_range=0.2,
                 height_shift_range=0.2,
                 fill_mode="nearest"
                 )
testgen = imgen(#rescale=1./255,
    preprocessing_function=keras.applications.efficienet_v2.preprocess_input )

# Data Generation train, test and validation

trainds = traingen.flow_from_directory("./Train-Test-Val/train",
                                       target_size = (224,224),
                                       seed = 123,
                                       batch_size = 32
                                       )


valds = valgen.flow_from_directory("./Train-Test-Val/val",
                                    target_size = (224,224),
                                    seed = 123,
                                    batch_size = 32
                                   )

testds = testgen.flow_from_directory("./Train-Test-Val/test",
                                     target_size = (224,224),
                                     batch_size = 32,
                                     shuffle = False
                                     )

print("Data Generated !!")

# Getting class names
classes = trainds.class_indices
classes = list(classes.keys())
print("The classes are : ",classes)



# MODEL CREATION

# Getting a pre-trained Model
print("Getting Pre Trained Model . . .")
base_model = EfficientNetV2S(include_top = False,
                      input_shape=(224,224,3),
                      weights="imagenet",
                      pooling="avg"
                      )
base_model.trainable = False

print("Model loaded!!")


# Defining a functional model
print("Building Model . .  .")

image_input = base_model.input
x = Dense(256,activation='relu')(base_model.output)
image_output = Dense(5,activation="softmax")(x)

model = Model(image_input,image_output)

print("Model built!! Summary is ===>")
print(model.summary())



# Compiling the model
print("Compiling . .  .")
model.compile(optimizer='adam',loss="categorical_crossentropy",metrics=["accuracy"])
print("Model Compiled!!")

# Defining callbacks and saving best model
my_calls = [EarlyStopping(monitor="val_accuracy",patience=4),
            ModelCheckpoint("Model_flower.h5",verbose= 1 ,save_best_only=True)]


# Training the model
print("Starting Training . . .")
hist = model.fit(trainds,epochs=18,validation_data=valds,callbacks=my_calls)
print("Model Trained!!")


# Testing the model
print("Testing score is ====>>")
model.evaluate(testds)


# Making predictions
print("Making predictions . . .")
pred = model.predict(testds,verbose=1)
pred = [np.argmax(i) for i in pred]
print("Done Predicting!!")

# Actual values
y_test = testds.classes


# Classification Report
print("Classification Report ::\n")
print(classification_report(pred,y_test))
print("\n\n")

# Confusion Matrix
print("Confusion Matrix is ::\n")
print(confusion_matrix(pred,y_test))