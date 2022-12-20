import numpy as np
from keras.models import load_model
from sklearn import datasets

'''
Iris Species
Classify iris plants into three species in this classic dataset
'''


class IrisService:
    def __init__(self):
        global model, graph, target_names
        model = load_model(r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\dlearn\iris\save\iris_model.h5')
        target_names = datasets.load_iris().target_names

    def service_model(self, features):
        features = np.reshape(features, (1, 4))
        Y_pred = model.predict(features, verbose=0)
        predicted = Y_pred.argmax(axis=-1)
        if predicted == 0:
            return 'setosa / 부채붓꽃'
        elif predicted == 1:
            return 'versicolor / 버시칼라'
        elif predicted == 2:
            return 'virginica / 버지니카'


IRIS_MENUS = ["종료", "보기"]
iris_menu = {
    "1": lambda x: x.service_model()
}

if __name__ == '__main__':
    def my_menu(ls):
        for i, j in enumerate(ls):
            print(f"{i}. {j}")
        return input('메뉴 선택: ')

    t = IrisService()
    while True:
        menu = my_menu(IRIS_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            iris_menu[menu](t)
