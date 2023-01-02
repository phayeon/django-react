import tensorflow.keras as keras
from tensorflow.keras.datasets import imdb
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.sequence import pad_sequences


class KoreanClassifyModel(object):
    def __init__(self):
        global train_input, train_target, test_input, test_target
        (train_input, train_target), (test_input, test_target) = imdb.load_data(
            num_words=500)  # 자주 등장하는 단어 500개만 사용, 매개 변수(num_words) 500으로 지정


if __name__ == '__main__':
    KoreanClassifyModel().fit_graph()
