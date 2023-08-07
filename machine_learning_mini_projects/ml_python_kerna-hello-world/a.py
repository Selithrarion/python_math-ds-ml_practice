import tensorflow as tf
import numpy as np
from tensorflow import keras

# regression problem + synthetic data
def main():
    bedrooms = np.array([2, 4, 5, 7, 11, 0])
    prices = np.array([150, 250, 300, 400, 600, 50])

    model = tf.keras.Sequential([
        keras.layers.Dense(units=1, input_shape=(1,))
    ])
    model.compile(optimizer=keras.optimizers.SGD(), loss=keras.losses.MeanSquaredError())
    model.fit(bedrooms, prices, epochs=500)

    print('8 bedroom house ', model.predict([10.0]))
    print('kernel', model.weights[0].numpy()[0, 0])
    print('bias', model.weights[1].numpy()[0])


main()
