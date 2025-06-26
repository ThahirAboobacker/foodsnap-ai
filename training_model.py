import matplotlib.pyplot as plt 
import numpy as np 
import PIL 
import tensorflow as tf 

from tensorflow import keras 
from tensorflow.keras import layers 
from tensorflow.keras.models import Sequential 

training_set=keras.utils.image_dataset_from_directory( 
  "/content/dataset", 
  labels="inferred", 
  label_mode="categorical", 
  class_names=None, 
  color_mode="rgb", 
  batch_size=32, 
  image_size=(256, 256), 
  shuffle=True, 
  seed=None, 
  validation_split=None, 
  subset=None, 
  interpolation="bilinear", 
  follow_links=False, 
  crop_to_aspect_ratio=False, 
  pad_to_aspect_ratio=False, 
  data_format=None, 
  verbose=True, 
) 
cnn=tf.keras.models.Sequential() 
cnn.add(tf.keras.layers.Conv2D(filters=32,kernel_size=3,activation='relu',input_shape=[256,256,3])) 
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2)) 
cnn.add(tf.keras.layers.Conv2D(filters=32,kernel_size=3,activation='relu')) 
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2)) 
cnn.add(tf.keras.layers.Dropout(0.5)) 
cnn.add(tf.keras.layers.Flatten()) 
cnn.add(tf.keras.layers.Dense(units=128,activation='relu')) 
cnn.add(tf.keras.layers.Dense(units=9,activation='softmax')) 
cnn.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy']) 
training_history=cnn.fit(x=training_set,epochs=30 ) 
cnn.save("fruit_classifier.h5")
