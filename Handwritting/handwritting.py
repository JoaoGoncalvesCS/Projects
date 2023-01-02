import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#Importing the training data
mnist = tf.keras.datasets.mnist

#Spliting the data into training data and testing data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#Normalizing the pixing values from 0 to 1
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

#Creating the model for the neural network
model = tf.keras.models.Sequential()

#Adding layers to the neural network model, 
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dense(10, activation="softmax"))

#Compiling the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

#Fitting the model(Training)

model.fit(x_train, y_train, epochs=3)

model.save("handwritten.model")

model = tf.keras.models.load_model("handwritten.model")

image_number = 1

while os.path.isfile(f"digits/digit{image_number}.png"):
    img = cv2.imread(f"digits/digit{image_number}.png")[:, :, 0]
    img = np.invert(np.array([img]))
    prediction = model.predict(img)
    print(f"This digit is probably a {np.argmax(prediction)}")
    plt.imshow(img[0], cmap=plt.cm.binary)
    plt.show()
    image_number += 1
