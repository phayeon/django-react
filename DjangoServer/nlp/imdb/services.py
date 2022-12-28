import time
from math import log, exp
from os import path
import csv

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from pandas._libs.internals import defaultdict
from selenium import webdriver


class ImdbService(object):
    def __init__(self):
        pass

class NaverMovieService(object):
    def __init__(self):
        global savepath, encoding, chrome_driver,naver_path, review_train, k, word_probs
        savepath = r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\nlp\imdb\save'
        encoding = "UTF-8"
        chrome_driver = r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\webcrawler\chromedriver.exe'
        naver_path = f'https://movie.naver.com/movie/point/af/list.naver?&page='
        review_train = r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\nlp\imdb\data\review_train.csv'
        k = 0.5
        word_probs = []

    def process(self, req):
        service = NaverMovieService()
        service.model_fit()
        result = service.classify(req)
        return result

    def crawling(self):
        if path.exists(f"{savepath}\\naver_movie_review.csv") == False:
            driver = webdriver.Chrome(chrome_driver)
            review_data = []

            for page in range(1, 10):
                driver.get(f'{naver_path}{page}')
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                # find_all : 지정한 태그의 내용을 모두 찾아 리스트로 반환
                all_tds = soup.find_all('td', attrs={'class', 'title'})
                # 한 페이지의 리뷰 리스트의 리뷰를 하나씩 보면서 데이터 추출

                for i in all_tds:
                    sentence = i.find("a", {"class": "report"}).get("onclick").split("', '")[2]
                    if sentence != "":  # 리뷰 내용이 비어있다면 데이터를 사용하지 않음
                        score = i.find("em").get_text()
                        review_data.append([sentence, int(score)])

            time.sleep(1)   # 다음 페이지를 조회하기 전 1초 시간 차를 두기

            with open(f'{savepath}\\naver_movie_review.csv', 'w', newline='', encoding=encoding) as f:
                wr = csv.writer(f)
                wr.writerows(review_data)
            driver.close()
            return "크롤링 완료"

        else:
            data = pd.read_csv(f"{savepath}\\naver_movie_review.csv", header=None)
            data.columns = ['review', 'score']
            result = [print(f"{i + 1}. {data['score'][i]}\n{data['review'][i]}\n") for i in range(len(data))]
            return result

    def load_corpus(self):
        corpus = pd.read_table(review_train, sep=",", encoding=encoding)
        corpus = np.array(corpus)
        return corpus

    def count_words(self, train_X):
        counts = defaultdict(lambda : [0, 0])
        for doc, point in train_X:
            if self.isNumber(doc) is False:
                words = doc.split()
                for word in words:
                    counts[word][0 if point > 3.5 else 1] += 1
            else:
                print('리뷰의 평점이 실수(float)로 되어 있지 않습니다.')
                break
        return counts

    def isNumber(self, param):
        try:
            float(param)
            return True
        except ValueError:
            return False

    def probability(self, word_probs, doc):
        docwords = doc.split()
        log_prob_if_class0 = log_prob_if_class1 = 0.0
        for word, prob_if_class0, prob_if_class1 in word_probs:
            if word in docwords:
                log_prob_if_class0 += log(prob_if_class0)
                log_prob_if_class1 += log(prob_if_class1)
            else:
                log_prob_if_class0 += log(1.0 - prob_if_class0)
                log_prob_if_class1 += log(1.0 - prob_if_class1)
        prob_if_class0 = exp(log_prob_if_class0)
        prob_if_class1 = exp(log_prob_if_class1)
        return prob_if_class0 / (prob_if_class0 + prob_if_class1)

    def word_probablities(self, counts, n_class0, n_class1, k):
        return [(w,
                 (class0 + k) / (n_class0 + 2 * k),
                 (class1 + k) / (n_class1 + 2 * k))
                for w, (class0, class1) in counts.items()]

    def classify(self, doc):
        return self.probability(word_probs=self.word_probs, doc=doc)

    def model_fit(self):
        train_X = self.load_corpus()
        '''
        '재밌네요': [1,0]
        '별로 재미없어요': [0,1]
        '''
        num_class0 = len([1 for _, point in train_X if point > 3.5])
        num_class1 = len(train_X) - num_class0
        word_counts = self.count_words(train_X)
        self.word_probs = self.word_probablities(word_counts, num_class0, num_class1, k)



if __name__ == '__main__':
    result = NaverMovieService().process('진짜 별로')
    print(f"긍정률 : {round(result, 2)}")
