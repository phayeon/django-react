import json
import warnings

import keras
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
from abc import abstractmethod, ABCMeta

from tensorflow.python.keras.models import load_model

warnings.filterwarnings('ignore')
import platform
import yfinance
from prophet import Prophet
from matplotlib import font_manager, rc, pyplot as plt

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
    def csv_read(self, **kwargs): pass


class AITraderModel(AITraderBase):
    def __init__(self):
        global start_data, end_data, item_code, path
        start_data = "2018-01-04"
        end_data = "2022-12-31"
        item_code = "AMD"
        path = r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\save'


    def hook(self, date):
        # self.npy_save()
        self.create_DNN_model(date)
        # self.create_LSTM_model(date)
        # self.ensemble_DNN(date)
        # self.ensemble_LSTM(date)
        print(data)
        return date

    def AMD_predict(self):
        yfinance.pdr_override() # 없으면 에러 발생
        item = data.get_data_yahoo(item_code, start=start_data, end=end_data)
        print(f' AMD head:{item.head(3)}')
        print(f' AMD tail:{item.tail(3)}')
        item['Close'].plot(figsize=(12, 6), grid=True)
        item_trunc = item[:'2022-12-31']
        df = pd.DataFrame({'ds': item_trunc.index, 'y': item_trunc['Close']})
        df.reset_index(inplace=True)
        del df['Date']
        prophet = Prophet(daily_seasonality=True)
        prophet.fit(df)
        future = prophet.make_future_dataframe(periods=61)
        forecast = prophet.predict(future)
        prophet.plot(forecast)
        plt.figure(figsize=(12, 6))
        plt.plot(item.index, item['Close'], label='real')
        plt.plot(forecast['ds'], forecast['yhat'], label='forecast')
        plt.grid()
        plt.legend()
        print(f'path: {path}')
        plt.savefig(f'{path}\\AMD_close.png')

    def csv_read(self):
        global KOSPI200, SAMSUNG
        KOSPI200 = pd.read_csv(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\data\코스피200.csv', index_col=0).dropna()
        SAMSUNG = pd.read_csv(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\data\삼성전자.csv', index_col=0).dropna()
        # print(KOSPI200.head(10))
        # print(SAMSUNG.head(10))

    def data_sort(self):
        self.csv_read()
        global KOSPI200, SAMSUNG

        print(KOSPI200.head(10))
        print(SAMSUNG.head(10))

        for i in range(KOSPI200.shape[0]):
            if '%' in KOSPI200.iloc[i, 5]:
                KOSPI200.iloc[i, 5] = float(KOSPI200.iloc[i, 5][0:len(KOSPI200.iloc[i, 5]) - 1])

        for i in range(SAMSUNG.shape[0]):
            if '%' in SAMSUNG.iloc[i, 5]:
                SAMSUNG.iloc[i, 5] = float(SAMSUNG.iloc[i, 5][0:len(SAMSUNG.iloc[i, 5]) - 1])
        '''
        for i in range(KOSPI200.shape[0]):
            if "-" in KOSPI200.iloc[i, 0]:
                KOSPI200.iloc[i, 0] = KOSPI200.iloc[i, 0].replace('- ', '')
                KOSPI200.iloc[i, 0] = pd.to_datetime(KOSPI200.iloc[i, 0], format='%Y%m%d')

        for i in range(SAMSUNG.shape[0]):
            if "-" in SAMSUNG.iloc[i, 0]:
                SAMSUNG.iloc[i, 0] = SAMSUNG.iloc[i, 0].replace('- ', '')
                SAMSUNG.iloc[i, 0] = pd.to_datetime(SAMSUNG.iloc[i, 0], format='%Y%m%d')
        '''

        for i in range(KOSPI200.shape[0]):
            if "M" in KOSPI200.iloc[i, 4]:
                KOSPI200.iloc[i, 4] = KOSPI200.iloc[i, 4].replace('M', '')
                KOSPI200.iloc[i, 4] = int(float(KOSPI200.iloc[i, 4]) * 1000000)
                for j in range(1, 4):
                    KOSPI200.iloc[i, j] = int(float(KOSPI200.iloc[i, j]) * 100)
            elif "K" in KOSPI200.iloc[i, 4]:
                KOSPI200.iloc[i, 4] = KOSPI200.iloc[i, 4].replace('K', '')
                KOSPI200.iloc[i, 4] = int(float(KOSPI200.iloc[i, 4]) * 1000)
                for j in range(1, 4):
                    KOSPI200.iloc[i, j] = int(float(KOSPI200.iloc[i, j]) * 100)

        for i in range(SAMSUNG.shape[0]):
            if "M" in SAMSUNG.iloc[i, 4]:
                SAMSUNG.iloc[i, 4] = SAMSUNG.iloc[i, 4].replace('M', '')
                SAMSUNG.iloc[i, 4] = int(float(SAMSUNG.iloc[i, 4]) * 1000000)
            elif "K" in SAMSUNG.iloc[i, 4]:
                SAMSUNG.iloc[i, 4] = SAMSUNG.iloc[i, 4].replace('K', '')
                SAMSUNG.iloc[i, 4] = int(float(SAMSUNG.iloc[i, 4]) * 1000)

        for i in range(KOSPI200.shape[0]):
            for j in range(0, 4):
                KOSPI200.iloc[i, j] = float(str(KOSPI200.iloc[i, j]).replace(',', ''))

        for i in range(SAMSUNG.shape[0]):
            for j in range(0, 4):
                SAMSUNG.iloc[i, j] = float(str(SAMSUNG.iloc[i, j]).replace(',', ''))

        KOSPI200 = KOSPI200.sort_values(['날짜'], ascending=[True])
        SAMSUNG = SAMSUNG.sort_values(['날짜'], ascending=[True])

        print(KOSPI200.head(10))
        print(SAMSUNG.head(10))

    def npy_save(self):
        self.data_sort()
        np.save(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\save\kospi200.npy', arr=KOSPI200.values)
        np.save(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\save\samsung.npy', arr=SAMSUNG.values)

    def npy_read(self):
        global KOSPI200, SAMSUNG
        KOSPI200 = np.load(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\save\kospi200.npy', allow_pickle=True)
        SAMSUNG = np.load(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\save\samsung.npy', allow_pickle=True)
        # print(KOSPI200.shape)
        # print(SAMSUNG.shape)

    def split_xy6(self, dataset, time_steps, y_column):
        x, y = list(), list()
        for i in range(len(dataset)):
            x_end_number = i + time_steps
            y_end_number = x_end_number + y_column

            if y_end_number > len(dataset):
                break
            tmp_x = dataset[i:x_end_number, :]
            tmp_y = dataset[x_end_number:y_end_number, 1]
            x.append(tmp_x)
            y.append(tmp_y)
        return np.array(x).astype(np.float32), np.array(y).astype(np.float32)

    def split_Common(self):
        self.npy_read()
        global x_train, x_test, y_train, y_test
        x, y = self.split_xy6(SAMSUNG, 6, 1)
        # print(x[0, :], '\n', y[0])
        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1] * x_train.shape[2]))
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1] * x_test.shape[2]))
        # print(x_train)
        # print(x_test)

    def split_LSTM(self):
        global x_train_scaled, x_test_scaled
        self.split_Common()
        x_train_scaled, x_test_scaled = self.preprocess(x_train, x_test)
        x_train_scaled = np.reshape(x_train_scaled, (x_train_scaled.shape[0], 6, 6))
        x_test_scaled = np.reshape(x_test_scaled, (x_test_scaled.shape[0], 6, 6))
        print(x_train_scaled.shape)
        print(x_test_scaled.shape)

    def preprocess(self, x_train, x_test):
        scaler = StandardScaler()
        scaler.fit(x_train)
        return scaler.transform(x_train), scaler.transform(x_test)


    def ensemble_common(self):
        global x1_train, x1_test, y1_train, y1_test, x2_train, x2_test, y2_train, y2_test
        self.npy_read()
        x1, y1 = self.split_xy6(SAMSUNG, 6, 3)
        x2, y2 = self.split_xy6(KOSPI200, 6, 3)
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


    def compile(self, date, x_train_scaled, x_test_scaled, y_train, y_test, model, filename):
        global data
        early_stopping = EarlyStopping(patience=20)
        model.fit(x_train_scaled, y_train, validation_split=0.2, verbose=1,
                  batch_size=1, epochs=1, callbacks=[early_stopping])

        loss, mse = model.evaluate(x_test_scaled, y_test, batch_size=1)
        print(f'loss : {loss}')
        print(f'mse : {mse}')

        y_pred = model.predict(x_test_scaled)

        data = []
        [data.append({'종가': json.dumps(y_test[i], cls=NumpyEncoder),
                      '예측가': json.dumps(y_pred[i], cls=NumpyEncoder)})
         for i in range(date)]

        model.save(f'{path}\\{filename}.h5')


class create_LSTM_model(AITraderModel):
    def creat(self):
        self.split_LSTM()
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
        self.compile(date, x_train_scaled, x_test_scaled, y_train, y_test, model, filename='LSTM_model')


class create_EnsembleDNN_model(AITraderModel):
    def creat(self):
        self.ensemble_common()

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

        self.compile(date, [x1_train_scaled, x2_train_scaled], [x1_test_scaled, x2_test_scaled],
                     y1_train, y1_test, model, filename='ensemble_DNN')


class create_EnsembleLSTM_model(AITraderModel):
    def creat(self):
        self.ensemble_common()

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

        self.compile(date, [x1_train_scaled, x2_train_scaled], [x1_test_scaled, x2_test_scaled],
                     y1_train, y1_test, model, filename='ensemble_LSTM')


if __name__ == '__main__':
    AITraderModel().hook(5)

