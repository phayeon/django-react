import json
import warnings
from enum import Enum

import numpy as np
import pandas as pd
from keras.callbacks import EarlyStopping
from keras.layers import Dense
from keras.models import Sequential
from numpyencoder import NumpyEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras import Input
from keras.callbacks import ModelCheckpoint
from keras.layers import LSTM, concatenate
from keras.models import Model
from abc import abstractmethod, ABCMeta, ABC
import platform
from matplotlib import font_manager, rc, pyplot as plt

warnings.filterwarnings('ignore')

path = "c:/Windows/Fonts/malgun.ttf"

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~')
plt.rcParams['axes.unicode_minus'] = False

'''
Date    Open     High      Low    Close     Adj Close   Volume
'''


class ModelType(Enum):
    dnn_model = 1
    dnn_ensemble = 2
    lstm_model = 3
    lstm_ensemble = 4


class H5FileNames(Enum):
    dnn_model = "DNN_model.h5"
    dnn_ensemble = "ensemble_DNN.h5"
    lstm_model = "LSTM_model.h5"
    lstm_ensemble = "ensemble_LSTM.h5"


class Activations(Enum):
    relu = 'relu'


class AITraderBase (metaclass=ABCMeta):
    @abstractmethod
    def hook(self, param): pass

    @abstractmethod
    def csv_structured(self): pass

    @abstractmethod
    def npy_save(self): pass

    @abstractmethod
    def npy_read(self): pass

    @abstractmethod
    def split_dataset(self): pass

    @abstractmethod
    def split_xy6(self, *args): pass

    @abstractmethod
    def split_ensemble(self): pass

    @abstractmethod
    def preprocess(self, *args): pass

    @abstractmethod
    def compile(self): pass

    @abstractmethod
    def predict(self, *args): pass


class AITraderModel(AITraderBase):
    @abstractmethod
    def hook(self, param): pass

    @abstractmethod
    def model(self): pass

    @abstractmethod
    def create(self): pass

    @abstractmethod
    def model_test(self, param): pass

    def __init__(self):
        global path, KOSPI200, SAMSUNG
        path = r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\save'
        KOSPI200 = pd.read_csv( r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\data\코스피200.csv',
                                index_col=0).dropna()
        SAMSUNG = pd.read_csv(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\data\삼성전자.csv',
                              index_col=0).dropna()

    def hook(self, date):
        # self.csv_structured()
        # self.npy_save()
        self.npy_read()
        self.split_dataset()

    def csv_structured(self):
        global KOSPI200, SAMSUNG

        data = [KOSPI200, SAMSUNG]

        for i in data:
            for j in range(i.shape[0]):
                if '%' in i.iloc[j, 5]:
                    i.iloc[j, 5] = float(i.iloc[j, 5][0:len(i.iloc[j, 5]) - 1])

            for j in range(i.shape[0]):
                if "M" in i.iloc[j, 4]:
                    i.iloc[j, 4] = i.iloc[j, 4].replace('M', '')
                    i.iloc[j, 4] = int(float(i.iloc[j, 4]) * 1000000)
                elif "K" in i.iloc[j, 4]:
                    i.iloc[j, 4] = i.iloc[j, 4].replace('K', '')
                    i.iloc[j, 4] = int(float(i.iloc[j, 4]) * 1000)

            for j in range(i.shape[0]):
                for k in range(0, 4):
                    i.iloc[j, k] = float(str(i.iloc[j, k]).replace(',', ''))
                    i.sort_values(['날짜'], ascending=[True])
            print(i.head(5))

    def npy_save(self):
        np.save(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\save\kospi200.npy',
                arr=KOSPI200.values)
        np.save(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\save\samsung.npy',
                arr=SAMSUNG.values)

    def npy_read(self):
        global KOSPI200, SAMSUNG
        KOSPI200 = np.load(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\save\kospi200.npy', allow_pickle=True)
        SAMSUNG = np.load(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\save\samsung.npy', allow_pickle=True)
        # print(KOSPI200.shape)
        # print(SAMSUNG.shape)

    def split_dataset(self):
        global x_train, x_test, y_train, y_test
        x, y = self.split_xy6(SAMSUNG, 6, 1)
        # print(x[0, :], '\n', y[0])
        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1] * x_train.shape[2]))
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1] * x_test.shape[2]))
        # print(x_train.shape)
        # print(x_test.shape)

    def split_xy6(self, *args):
        x, y = list(), list()
        for i in range(len(args[0])):
            x_end_number = i + args[1]
            y_end_number = x_end_number + args[2]

            if y_end_number > len(args[0]):
                break
            tmp_x = args[0][i:x_end_number, :]
            tmp_y = args[0][x_end_number:y_end_number, 1]
            x.append(tmp_x)
            y.append(tmp_y)
        return np.array(x).astype(np.float32), np.array(y).astype(np.float32)

    def split_ensemble(self):
        global x1_train, x1_test, y1_train, y1_test, x2_train, x2_test, y2_train, y2_test
        x1, y1 = self.split_xy6(SAMSUNG, 6, 1)
        x2, y2 = self.split_xy6(KOSPI200, 6, 1)
        # print(x2[0, :], '\n', y2[0])
        # print(x2.shape)

        x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, random_state=1, test_size=0.3)
        x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, random_state=2, test_size=0.3)
        # print(x2_train.shape)

        x1_train = np.reshape(x1_train, (x1_train.shape[0], x1_train.shape[1] * x1_train.shape[2]))
        x1_test = np.reshape(x1_test, (x1_test.shape[0], x1_test.shape[1] * x1_test.shape[2]))
        x2_train = np.reshape(x2_train, (x2_train.shape[0], x2_train.shape[1] * x2_train.shape[2]))
        x2_test = np.reshape(x2_test, (x2_test.shape[0], x2_test.shape[1] * x2_test.shape[2]))
        # print(x2_train.shape)

    def preprocess(self, *args):
        scaler = StandardScaler()
        scaler.fit(args[0])
        return scaler.transform(args[0]), scaler.transform(args[1])

    def compile(self, *args):
        early_stopping = EarlyStopping(patience=20)
        args[0].fit(args[1], args[3], validation_split=0.2, verbose=1,
                  batch_size=1, epochs=100, callbacks=[early_stopping])

        loss, mse = args[0].evaluate(args[2], args[4], batch_size=1)
        print(f'loss :{loss} / mse :{mse}')

        y_pred = args[0].predict(args[2])

        data = []
        [data.append({'종가': json.dumps(args[4][i], cls=NumpyEncoder),
                      '예측가': json.dumps(y_pred[i], cls=NumpyEncoder)})
         for i in range(5)]

        print(data)
        args[0].save(f'{path}\\{args[5]}')

    def predict(self, *args):
        global data
        model.load_weights(f'{path}\\{args[3]}')
        loss, mse = args[0].evaluate(args[1], args[2], batch_size=1)
        print(f'loss :{loss} / mse :{mse}')

        y_pred = args[0].predict(args[1])

        data = []
        [data.append({'종가': json.dumps(args[2][i], cls=NumpyEncoder),
                      '예측가': json.dumps(y_pred[i], cls=NumpyEncoder)})
         for i in range(args[4])]

        print(data)
        return data


class create_DNN_model(AITraderModel):
    def hook(self, date):
        super().npy_read()
        super().split_dataset()
        self.model()
        # self.create()
        self.model_test(date)
        return data

    def model(self):
        global model, x_train_scaled, x_test_scaled, filename

        x_train_scaled, x_test_scaled = super().preprocess(x_train, x_test)
        # print(x_train_scaled[0, :])

        model = Sequential()
        model.add(Dense(64, input_shape=(36,)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))
        model.compile(loss='mse',
                      optimizer='adam',
                      metrics=['mse'])

        filename = H5FileNames.dnn_model

    def create(self):
        super().compile(model, x_train_scaled, x_test_scaled, y_train, y_test, filename)

    def model_test(self, date):
        super().predict(model, x_test_scaled, y_test, filename, date)


class create_LSTM_model(AITraderModel):
    def hook(self, date):
        super().npy_read()
        super().split_dataset()
        self.model()
        # self.create()
        self.model_test(date)
        return data

    def model(self):
        global model, x_train_scaled, x_test_scaled, filename

        x_train_scaled, x_test_scaled = super().preprocess(x_train, x_test)
        # print(x_train_scaled[0, :])

        x_train_scaled = np.reshape(x_train_scaled, (x_train_scaled.shape[0], 6, 6))
        x_test_scaled = np.reshape(x_test_scaled, (x_test_scaled.shape[0], 6, 6))

        model = Sequential()
        model.add(LSTM(64, input_shape=(6, 6)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))
        model.compile(loss='mse',
                      optimizer='adam',
                      metrics=['mse'])

        filename = H5FileNames.lstm_model

    def create(self):
        super().compile(model, x_train_scaled, x_test_scaled, y_train, y_test, filename)

    def model_test(self, date):
        super().predict(model, x_test_scaled, y_test, filename, date)


class create_DNN_Emsemble(AITraderModel):
    def hook(self, date):
        super().npy_read()
        super().split_dataset()
        super().split_ensemble()
        self.model()
        # self.create()
        self.model_test(date)
        return data

    def model(self):
        global model, x1_train_scaled, x1_test_scaled, x2_train_scaled, x2_test_scaled, filename
        x1_train_scaled, x1_test_scaled = self.preprocess(x1_train, x1_test)
        x2_train_scaled, x2_test_scaled = self.preprocess(x2_train, x2_test)
        # print(x2_train_scaled[0, :])

        input1 = Input(shape=(36,))
        dense1 = Dense(64)(input1)
        dense1 = Dense(32)(dense1)
        dense1 = Dense(32)(dense1)
        output1 = Dense(32)(dense1)

        input2 = Input(shape=(36,))
        dense2 = Dense(64)(input2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        output2 = Dense(32)(dense2)

        merge = concatenate([output1, output2])
        output3 = Dense(1)(merge)

        model = Model(inputs=[input1, input2], outputs=output3)
        model.compile(loss='mse', optimizer='adam', metrics=['mse'])

        filename = H5FileNames.dnn_ensemble

    def create(self):
        super().compile(model, [x1_train_scaled, x2_train_scaled], [x1_test_scaled, x2_test_scaled],
                        y1_train, y1_test, filename)

    def model_test(self, date):
        super().predict(model, [x1_test_scaled, x2_test_scaled], y1_test, filename, date)


class create_LSTM_Emsemble(AITraderModel):
    def hook(self, date):
        super().npy_read()
        super().split_dataset()
        super().split_ensemble()
        self.model()
        # self.create()
        self.model_test(date)
        return data

    def model(self):
        global model, x1_train_scaled, x1_test_scaled, x2_train_scaled, x2_test_scaled, filename
        x1_train_scaled, x1_test_scaled = self.preprocess(x1_train, x1_test)
        x2_train_scaled, x2_test_scaled = self.preprocess(x2_train, x2_test)
        # print(x2_train_scaled[0, :])

        x1_train_scaled = np.reshape(x1_train_scaled, (x1_train_scaled.shape[0], 6, 6))
        x1_test_scaled = np.reshape(x1_test_scaled, (x1_test_scaled.shape[0], 6, 6))
        x2_train_scaled = np.reshape(x2_train_scaled, (x2_train_scaled.shape[0], 6, 6))
        x2_test_scaled = np.reshape(x2_test_scaled, (x2_test_scaled.shape[0], 6, 6))

        input1 = Input(shape=(6, 6))
        dense1 = LSTM(64)(input1)
        dense1 = Dense(32)(dense1)
        dense1 = Dense(32)(dense1)
        output1 = Dense(32)(dense1)

        input2 = Input(shape=(6, 6))
        dense2 = LSTM(64)(input2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        output2 = Dense(32)(dense2)

        merge = concatenate([output1, output2])
        output3 = Dense(1)(merge)

        model = Model(inputs=[input1, input2], outputs=output3)
        model.compile(loss='mse', optimizer='adam', metrics=['mse'])

        filename = H5FileNames.lstm_ensemble

    def create(self):
        super().compile(model, [x1_train_scaled, x2_train_scaled], [x1_test_scaled, x2_test_scaled],
                        y1_train, y1_test, filename)

    def model_test(self, date):
        super().predict(model, [x1_test_scaled, x2_test_scaled], y1_test, filename, date)


if __name__ == '__main__':
    # create_DNN_model().hook(5)
    # create_LSTM_model().hook(5)
    # create_DNN_Emsemble().hook(5)
    create_LSTM_Emsemble().hook(2)
