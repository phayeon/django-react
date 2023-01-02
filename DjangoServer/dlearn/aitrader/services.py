import warnings

import numpy as np
import pandas as pd
from keras.callbacks import EarlyStopping
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
warnings.filterwarnings('ignore')
import pandas_datareader.data as web
from pandas_datareader import data
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

class AITraderService(object):
    def __init__(self):
        global start_data, end_data, item_code
        start_data = "2018-01-04"
        end_data = "2022-12-31"
        item_code = "AMD"

    def hook(self):
        self.npy_save()
        self.compile()

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
        path = r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\save'
        print(f'path: {path}')
        plt.savefig(f'{path}\\AMD_close.png')

    def csv_read(self):
        global KOSPI200, SAMSUNG
        KOSPI200 = pd.read_csv(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\data\삼성전자.csv', index_col=0)
        SAMSUNG = pd.read_csv(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\aitrader\data\005930 역사적 데이터.csv', index_col=0)
        # print(KOSPI200)
        # print(SAMSUNG)

    def data_sort(self):
        self.csv_read()
        global KOSPI200, SAMSUNG

        for i in range(601):
            if pd.isna(SAMSUNG['거래량'][i]) == False:
                SAMSUNG['거래량'][i] = float(SAMSUNG['거래량'][i][0:len(SAMSUNG['거래량'][i])-1])
            else:
                SAMSUNG['거래량'][i] = 0

        for i in range(601):
            if pd.isna(SAMSUNG['변동 %'][i]) == True:
                SAMSUNG['변동 %'][i] = 0
            else:
                SAMSUNG['변동 %'][i] = float(SAMSUNG['변동 %'][i][0:len(SAMSUNG['변동 %'][i])-1])

        for i in range(600):
            if pd.isna(KOSPI200['거래량'][i]) == False:
                KOSPI200['거래량'][i] = float(KOSPI200['거래량'][i][0:len(KOSPI200['거래량'][i])-1])
            else:
                KOSPI200['거래량'][i] = 0

        for i in range(600):
            if pd.isna(KOSPI200['변동 %'][i]) == True:
                KOSPI200['변동 %'][i] = 0
            else:
                KOSPI200['변동 %'][i] = float(KOSPI200['변동 %'][i][0:len(KOSPI200['변동 %'][i])-1])

        for i in range(601):
            for j in range(0, 4):
                SAMSUNG.iloc[i, j] = float(SAMSUNG.iloc[i, j].replace(',', ''))

        for i in range(600):
            for j in range(0, 4):
                KOSPI200.iloc[i, j] = float(KOSPI200.iloc[i, j].replace(',', ''))

        KOSPI200 = KOSPI200.sort_values(['날짜'], ascending=[True])
        SAMSUNG = SAMSUNG.sort_values(['날짜'], ascending=[True])

        print(KOSPI200.head(3))
        print(SAMSUNG.head(6))


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

    def data_split(self):
        self.npy_read()
        global x_train, x_test, y_train, y_test
        x, y = self.split_xy6(SAMSUNG, 6, 1)
        # print(x[0, :], '\n', y[0])
        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1] * x_train.shape[2]))
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1] * x_test.shape[2]))
        print(x_train)
        print(x_test)

    def preprocess(self):
        global x_train_scaled, x_test_scaled
        self.data_split()
        scaler = StandardScaler()
        scaler.fit(x_train)
        x_train_scaled = scaler.transform(x_train)
        x_test_scaled = scaler.transform(x_test)
        print(x_train_scaled[0, :])

    def create_model(self):
        global model
        model = Sequential()
        model.add(Dense(256, input_shape=(x_train.shape[1],), activation='sigmoid'))
        model.add(Dense(64, input_shape=(25,)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))
        model.compile(loss='mse',
                      optimizer='adam',
                      metrics=['mse'])

    def compile(self):
        self.preprocess()
        self.create_model()
        early_stopping = EarlyStopping(patience=20)
        model.fit(x_train_scaled, y_train, validation_split=0.2, verbose=1,
                  batch_size=1, epochs=100, callbacks=[early_stopping])

        loss, mse = model.evaluate(x_test_scaled, y_test, batch_size=1)
        print(f'loss : {loss}')
        print(f'mse : {mse}')

        y_pred = model.predict(x_test_scaled)

        for i in range(5):
            print(f'종가 :{y_test[i]}\n예측가 :{y_pred[i]}')


if __name__ == '__main__':
    AITraderService().hook()
