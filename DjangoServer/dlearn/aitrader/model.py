import json
import warnings

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


class AITraderBase (metaclass=ABCMeta):
    @abstractmethod
    def csv_structured(self): pass


class AITraderModel(AITraderBase, ABC):
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
        # create_LSTM_model().create()
        create_LSTM_model().model_test(date)

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

    def preprocess(self, *args):
        scaler = StandardScaler()
        scaler.fit(args[0])
        return scaler.transform(args[0]), scaler.transform(args[1])

    def compile(self, *args):
        early_stopping = EarlyStopping(patience=20)
        args[0].fit(args[1], y_train, validation_split=0.2, verbose=1,
                  batch_size=1, epochs=100, callbacks=[early_stopping])

        loss, mse = args[0].evaluate(args[2], y_test, batch_size=1)
        print(f'loss :{loss} / mse :{mse}')

        y_pred = args[0].predict(args[2])

        data = []
        [data.append({'종가': json.dumps(y_test[i], cls=NumpyEncoder),
                      '예측가': json.dumps(y_pred[i], cls=NumpyEncoder)})
         for i in range(5)]

        args[0].save(f'{path}\\{args[3]}.h5')

    def predict(self, *args):
        model.load_weights(f'{path}\\{args[2]}.h5')
        loss, mse = args[0].evaluate(args[1], y_test, batch_size=1)
        print(f'loss :{loss} / mse :{mse}')

        y_pred = args[0].predict(args[1])

        data = []
        [data.append({'종가': json.dumps(y_test[i], cls=NumpyEncoder),
                            '예측가': json.dumps(y_pred[i], cls=NumpyEncoder)})
               for i in range(args[3])]

        print(data)


class create_DNN_model(AITraderModel):
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

        filename = 'DNN_model'

    def create(self):
        self.model()
        super().compile(model, x_train_scaled, x_test_scaled, filename)

    def model_test(self, date):
        self.model()
        super().predict(model, x_test_scaled, filename, date)


class create_LSTM_model(AITraderModel):
    def model(self):
        global model, x_train_scaled, x_test_scaled, filename

        x_train_scaled, x_test_scaled = super().preprocess(x_train, x_test)
        # print(x_train_scaled[0, :])

        x_train_scaled = np.reshape(x_train_scaled, (x_train_scaled.shape[0], 6, 6))
        x_test_scaled = np.reshape(x_test_scaled, (x_test_scaled.shape[0], 6, 6))

        filename = 'LSTM_model'
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

    def create(self):
        self.model()
        super().compile(model, x_train_scaled, x_test_scaled, filename)

    def model_test(self, date):
        self.model()
        super().predict(model, x_test_scaled, filename, date)



if __name__ == '__main__':
    AITraderModel().hook(5)
