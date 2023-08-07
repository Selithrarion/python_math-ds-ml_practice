from tensorflow import keras
import tensorflow as tf
import matplotlib.pyplot as plt


# image recognition + real data
def main():
    trained_model, test_images, test_labels = get_trained_model()
    export_model_history_graph(trained_model)
    trained_model.evaluate(test_images, test_labels)


def get_trained_model():
    mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    # 255 to 1 etc
    train_images = train_images / 255.0
    test_images = test_images / 255.0

    model = keras.models.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(256, activation=keras.activations.relu),
        keras.layers.Dense(10, activation=keras.activations.softmax)
    ])
    # print(model.summary())
    model.compile(optimizer=keras.optimizers.Adam(), loss=keras.losses.sparse_categorical_crossentropy,
                  metrics=['accuracy'])
    model.fit(train_images, train_labels, epochs=5, validation_data=(test_images, test_labels))

    return model, test_images, test_labels


def export_model_history_graph(model):
    plt.plot(model.history.history['accuracy'], label='Train acc')
    plt.plot(model.history.history['val_accuracy'], label='Test acc')
    plt.xlabel('Epochs')
    plt.ylabel('Acc')
    plt.legend()
    plt.savefig('c_acc_plot')

    plt.close()
    plt.plot(model.history.history['loss'], label='Train loss')
    plt.plot(model.history.history['val_loss'], label='Test loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig('c_loss_plot.png')


main()
