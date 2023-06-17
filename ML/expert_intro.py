#!/usr/bin/env python3

import tensorflow as tf

from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model

#get MNIST dataset link

mnist = tf.keras.datasets.mnist

#Load data

(x_train, y_train), (x_test, y_test) = mnist.load_data()
#scale input data
x_train = x_train / 255
y_train = y_train / 255

# Add a new dimension
x_train=x_train[...,tf.newaxis].astype("float32")
x_test =x_test[..., tf.newaxis].astype("float32")

#Shuffle the data and make batches
train_da = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(32)
test_da  = tf.data.Dataset.from_tensor_slices((x_test , y_test )).shuffle(10000).batch(32)

#Build tf.keras model using the keras model subclassing API

class MyModel(Mode):
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = Conv2D(32,3,activation='relu')
        self.flatten = Flatten()
        self.d1 = Dense(128, activation='relue')
        self.d2 = Dense(10)
