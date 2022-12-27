import time
from os import path
import csv
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


class ImdbService(object):
    def __init__(self):
        pass

class NaverMovieService(object):
    def __init__(self):
        global savepath, encoding, chrome_driver,naver_path
        savepath = r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\nlp\imdb\save'
        encoding = "UTF-8"
        chrome_driver = r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\webcrawler\chromedriver.exe'
        naver_path = f'https://movie.naver.com/movie/point/af/list.naver?&page='

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


if __name__ == '__main__':
    NaverMovieService().crawling()
