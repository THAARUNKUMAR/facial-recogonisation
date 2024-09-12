from google.colab import drive
drive.mount('/content/drive')
import os
path = '/content/drive/MyDrive/face1/Train'
classes = os.listdir(path)
print(classes)

from tensorflow.keras.preprocessing import image_dataset_from_directory

base_dir = '/content/drive/MyDrive/face1'

# Create datasets
train_datagen = image_dataset_from_directory(base_dir,
image_size=(200,200),
subset='training',
seed = 1,
validation_split=0.1,
       batch_size= 32)

test_datagen = image_dataset_from_directory(base_dir,
image_size=(200,200),
subset='validation',
seed = 1,
validation_split=0.1,
batch_size= 32)

import tensorflow as tf

from tensorflow import keras
from keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras.layers import Conv2D, MaxPooling2D


model = tf.keras.models.Sequential([
layers.Conv2D(32, (3, 3), activation='relu', input_shape=(200, 200, 3)),
layers.MaxPooling2D(2, 2),
layers.Conv2D(64, (3, 3), activation='relu'),
layers.MaxPooling2D(2, 2),
layers.Conv2D(64, (3, 3), activation='relu'),
layers.MaxPooling2D(2, 2),
layers.Conv2D(64, (3, 3), activation='relu'),
layers.MaxPooling2D(2, 2),

layers.Flatten(),
layers.Dense(512, activation='relu'),
layers.BatchNormalization(),
layers.Dense(512, activation='relu'),
layers.Dropout(0.1),
layers.BatchNormalization(),
layers.Dense(512, activation='relu'),
layers.Dropout(0.2),
layers.BatchNormalization(),
layers.Dense(1, activation='sigmoid') #output layer
])

keras.utils.plot_model(
model,
show_shapes=True,
show_dtype=True,
show_layer_activations=True
)
model.compile(
loss='binary_crossentropy',
optimizer='adam',
metrics=['accuracy']
)
history = model.fit(train_datagen,
epochs=10,
validation_data=test_datagen)
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

test_image= image.load_img("/content/drive/MyDrive/R.png",target_size=(200,200))
plt.imshow(test_image)
test_image=image.img_to_array(test_image)
test_image=np.expand_dims(test_image,axis=0)
result=model.predict(test_image)
print(result)

if(result==1):
  print("C")
else:
  print("R")
