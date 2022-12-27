import tensorflow.keras as keras
from tensorflow.keras.datasets import imdb
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.sequence import pad_sequences


class ImdbModel(object):
    def __init__(self):
        global train_input, train_target, test_input, test_target
        (train_input, train_target), (test_input, test_target) = imdb.load_data(
            num_words=500)  # 자주 등장하는 단어 500개만 사용, 매개 변수(num_words) 500으로 지정

    def imdb_info(self):
        print("훈련 데이터 사이즈", train_input.shape, "\n테스트 데이터 사이즈", test_input.shape)
        print("첫 번째 리뷰의 길이 :", len(train_input[0]))
        print("두 번째 리뷰의 길이 :", len(train_input[1]))
        print("##### 첫 번째 리뷰 #####\n", train_input[0])
        print("##### 타깃 데이터 #####\n", train_target[:20])

    def data_split(self):
        global train_input, train_target, val_input, val_target, lengths
        train_input, val_input, train_target, val_target = train_test_split(
            train_input, train_target, test_size=0.2, random_state=42)
        # print("훈련 데이터 사이즈", train_input.shape, "\n테스트 데이터 사이즈", test_input.shape)
        lengths = np.array([len(x) for x in train_input])
        # print("리뷰 길이 평균 값 : ", np.mean(lengths), "\n리뷰 길이 중간 값 : ", np.median(lengths))

    def length_histogram(self):
        self.data_split()
        plt.hist(lengths)
        plt.xlabel('length')
        plt.ylabel('frequency')
        plt.show()

    def imdb_pad_sequence(self):
        global train_seq, val_seq
        self.data_split()
        train_seq = pad_sequences(train_input, maxlen=100, truncating='pre')    # 뒷 부분에 패딩을 넣고 싶으면 truncating='post'로 변경
        # print("train_seq의 길이 :", train_seq.shape)
        # print("##### 첫 번째 샘플 #####\n", train_seq[0])  # 길이가 100 이상인 리뷰
        # print("##### 여섯 번째 샘플 #####\n", train_seq[5]) # 길이가 100 이하인 리뷰
        # print("##### 원본 데이터 확인 #####\n", train_input[0][-10:])
        val_seq = pad_sequences(val_input, maxlen=100)

    def creat_RNN(self):
        global model, train_oh, val_oh
        self.imdb_pad_sequence()
        model = keras.Sequential()
        sample_length = 100 # 샘플의 길이
        freq_words = 500    # 사용 빈도 높은 단어 개수

        model.add(keras.layers.SimpleRNN(8, input_shape=(sample_length, freq_words)))
        model.add(keras.layers.Dense(1, activation='sigmoid'))

        train_oh = keras.utils.to_categorical(train_seq)
        val_oh = keras.utils.to_categorical(val_seq)

        print("##### oh 배열의 크기 #####\n", train_oh.shape)    # oh is OneHotEncoding
        print("##### 인코딩 확인 #####\n", train_oh[0][0][:12])
        print("##### 모델 구조 출력 #####\n", model.summary())

    def fit(self):
        global history
        self.creat_RNN
        rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
        model.compile(optimizer=rmsprop, loss='binary_crossentropy', metrics=['accuracy'])
        checkpoint_cb = keras.callbacks.ModelCheckpoint('best-simplernn-model.h5',
                                                        save_best_only=True)
        early_stopping_cd = keras.callbacks.EarlyStopping(patience=3,
                                                          restore_best_weights=True)
        history = model.fit(train_oh, train_target, epochs=10, batch_size=64,
                            validation_data=(val_oh, val_target),
                            callbacks=[checkpoint_cb, early_stopping_cd])

    def fit_graph(self):
        self.creat_RNN()
        self.fit()
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.xlabel('epoch')
        plt.ylabel('loss')
        plt.legend(['train', 'val'])
        plt.show()

        print("train_seq의 크기 :", train_seq.nbytes, "\ntrain_oh의 크기 :", train_oh.nbytes)


class NaverMovieModel(object):
    def __init__(self):
        pass

    def word_embedding(self):
        global model2
        model2 = keras.Sequential()
        model2.add(keras.layers.Embedding(500, 16, input_length=100))
        model2.add(keras.layers.SimpleRNN(8))
        model2.add(keras.layers.Dense(1, activation='sigmoid'))
        print("##### 모델 구조 출력 #####\n", model2.summary())

    def embedding_fit(self):
        self.word_embedding()
        rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
        model2.compile(optimizer=rmsprop, loss='binary_crossentropy',
                       metrics=['accuracy'])
        checkpoint_cb = keras.callbacks.ModelCheckpoint('best-embedding-model.h5',
                                                        save_best_only=True)
        early_stopping_cd = keras.callbacks.EarlyStopping(patience=3,
                                                          restore_best_weights=True)
        history = model2.fit(train_seq)




if __name__ == '__main__':
    import tensorflow
    ImdbModel().fit_graph()
