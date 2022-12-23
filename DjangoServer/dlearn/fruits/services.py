import os

import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras import layers
from tensorflow import keras
from keras.callbacks import ModelCheckpoint

class FruitsService:
    def __init__(self):
        global class_names, trainpath, testpath, Apple_Braeburn_train, \
            Apple_Crimson_Snow_train, Apple_Golden_1_train, Apple_Golden_2_train, \
            Apple_Golden_3_train, Apple_Braeburn_test, Apple_Crimson_Snow_test, \
            Apple_Golden_1_test, Apple_Golden_2_test, Apple_Golden_3_test, \
            batchsize, img_height, img_width

        trainpath = r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\fruits\data\Training'
        testpath = r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\fruits\data\Test'
        Apple_Braeburn_train = f'{trainpath}\\Apple Braeburn'
        Apple_Crimson_Snow_train = f'{trainpath}\\Apple Crimson Snow'
        Apple_Golden_1_train = f'{trainpath}\\Apple Golden 1'
        Apple_Golden_2_train = f'{trainpath}\\Apple Golden 2'
        Apple_Golden_3_train = f'{trainpath}\\Apple Golden 3'
        Apple_Braeburn_test = f'{testpath}\\Apple Braeburn'
        Apple_Crimson_Snow_test = f'{testpath}\\Apple Crimson Snow'
        Apple_Golden_1_test = f'{testpath}\\Apple Golden 1'
        Apple_Golden_2_test = f'{testpath}\\Apple Golden 2'
        Apple_Golden_3_test = f'{testpath}\\Apple Golden 3'
        batchsize = 32
        img_height = 100
        img_width = 100

    def hook(self):
        self.show_model_graph()

    def show_apple(self):
        img = tf.keras.preprocessing.image.load_img\
            (f'{Apple_Braeburn_test}\\3_100.jpg')

        class_name = os.listdir(testpath)

        plt.figure(figsize=(3, 3))
        plt.imshow(img)
        plt.title(class_name[0])
        plt.axis("off")
        plt.show()

    def dateset_concat(self):
        global x, y, class_names, train_ds, val_ds, test_ds, test_ds1

        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            trainpath, validation_split=0.3, subset="validation", seed=1, image_size=(img_height, img_width),
            batch_size=batchsize)
        val_ds = tf.keras.preprocessing.image_dataset_from_directory(
            trainpath, validation_split=0.3, subset="validation", seed=1, image_size=(img_height, img_width),
            batch_size=batchsize)
        class_names = train_ds.class_names
        test_ds = tf.keras.preprocessing.image_dataset_from_directory(
            testpath, seed=1, image_size=(img_height, img_width), batch_size=batchsize)
        test_ds1 = tf.keras.preprocessing.image_dataset_from_directory(
            testpath, seed=1, image_size=(img_height, img_width), batch_size=batchsize, shuffle=False)

        y = np.concatenate([y for x, y in test_ds], axis=0)
        y = np.concatenate([y for x, y in test_ds1], axis=0)
        x = np.concatenate([x for x, y in test_ds1], axis=0)

    def show_title_img(self):
        self.dateset_concat()
        plt.figure(figsize=(3, 3))
        plt.imshow(x[-1].astype("uint8"))
        plt.title(class_names[y[-1]])
        plt.axis("off")
        plt.show()

    def modify_prefetch(self):
        global train_p, val_p, test_p

        self.dateset_concat()
        BUFFER_SIZE = 10000
        AUTOTUNE = tf.data.experimental.AUTOTUNE

        train_p = train_ds.cache().shuffle(BUFFER_SIZE).prefetch(buffer_size=AUTOTUNE)
        val_p = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
        test_p = test_ds.cache().prefetch(buffer_size=AUTOTUNE)

    def create_cnn_model(self):
        global model
        num_classes = 5
        model = tf.keras.Sequential([
            layers.experimental.preprocessing.Rescaling(1./255, input_shape=(img_height,
                                                                             img_width, 3)),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(2),
            layers.Dropout(.50),
            layers.Conv2D(32, 2, padding='same', activation='relu'),
            layers.MaxPooling2D(2),
            layers.Dropout(.50),
            layers.Flatten(),
            layers.Dense(500, activation='relu'),
            layers.Dropout(.50),
            layers.Dense(num_classes, activation='softmax')
        ])
        model.compile(
            optimizer='adam',
            loss=tf.losses.SparseCategoricalCrossentropy(),
            metrics=['accuracy']
        )

    def learn_model(self):
        global history
        self.modify_prefetch()
        self.create_cnn_model()
        checkpointer = ModelCheckpoint(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\fruits\save\CNNclassifier.h5',
                                       save_best_only=True)
        early_stopping_cb = keras.callbacks.EarlyStopping(patience=5,
                                                          monitor='val_accuracy',
                                                          restore_best_weights=True)
        epochs = 20
        history = model.fit(
            train_p,
            batch_size=batchsize,
            validation_data=val_ds,
            epochs=epochs,
            callbacks=[checkpointer, early_stopping_cb]
        )

    def show_model_graph(self):
        self.learn_model()
        epoch_num = int(input("epoch 횟수 : "))

        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']
        loss = history.history['loss']
        val_loss = history.history['val_loss']
        epochs_range = range(1, epoch_num+1)

        plt.figure(figsize=(10, 5))
        plt.subplot(121)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        plt.subplot(122)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')

        plt.show()

    def load_weights(self):
        self.modify_prefetch()
        self.create_cnn_model()
        model.load_weights(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\fruits\save\CNNclassifier.h5')

    def show_model_predict(self):
        self.load_weights()
        test_loss, test_acc = model.evaluate(test_ds)

        print("test loss : ", test_loss)
        print("test acc : ", test_acc)

    def test_predict(self):
        self.load_weights()
        predictions = model.predict(test_ds1)
        score1 = tf.nn.softmax(predictions[0])
        score2 = tf.nn.softmax(predictions[-1])

        print(f"This image most likely belongs to '{class_names[np.argmax(score1)]}'"
              f" with a {100 * np.max(score1)} precent confidence.")
        print(f"This image most likely belongs to '{class_names[np.argmax(score2)]}'"
              f" with a {100 * np.max(score2)} precent confidence.")


if __name__ == '__main__':
    FruitsService().hook()
