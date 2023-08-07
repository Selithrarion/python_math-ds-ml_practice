from tensorflow import keras

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


# classification problem + real data
def main():
    trained_model = get_trained_model()
    export_model_history_graph(trained_model)


def get_trained_model():
    data = load_iris()

    x = data['data']
    y = data['target']
    # print('data', x[0], y[0])

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    # print('training data', x_train.shape)
    # print('training targets', y_train.shape)
    # print('test data', x_test.shape)
    # print('test targets', y_test.shape)

    model = keras.models.Sequential([
        keras.layers.Dense(units=10, activation=keras.activations.relu, input_shape=(4,)),
        keras.layers.Dense(units=3, activation=keras.activations.softmax)
    ])

    # print(model.summary())

    model.compile(optimizer=keras.optimizers.RMSprop(), loss=keras.losses.sparse_categorical_crossentropy,
                  metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=100, validation_data=(x_test, y_test))

    return model


def export_model_history_graph(model):
    plt.plot(model.history.history['accuracy'], label='Train acc')
    plt.plot(model.history.history['val_accuracy'], label='Test acc')
    plt.xlabel('Epochs')
    plt.ylabel('Acc')
    plt.legend()
    plt.savefig('b_acc_plot.png')

    plt.close()
    plt.plot(model.history.history['loss'], label='Train loss')
    plt.plot(model.history.history['val_loss'], label='Test loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig('b_loss_plot.png')


main()
