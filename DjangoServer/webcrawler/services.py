import csv
import urllib
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os.path
from os import path


class ScrapService(object):
    def __init__(self):
        global driverpath, naver_url, savepath, encoding
        driverpath = r"C:\Users\AIA\PycharmProjects\django-react\DjangoServer\webcrawler\chromedriver"
        savepath = r"C:\Users\AIA\PycharmProjects\django-react\DjangoServer\webcrawler\save"
        naver_url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
        encoding = "UTF-8"

    def melon_music(self, *params):   # BeautifulSoup 기본 크롤링
        urlheader = urllib.request.Request(params[0].domain, headers={'User-Agent': "Mozilla/5.0"})
        htmlurl = urllib.request.urlopen(urlheader).read()
        soup = BeautifulSoup(htmlurl, "lxml")

        title = {"class": params[0].class_names[0]}
        artist = {"class": params[0].class_names[1]}
        titles = soup.find_all(name=params[0].tag_name, attrs=title)
        titles = [i.find('a').text for i in titles]
        artists = soup.find_all(name=params[0].tag_name, attrs=artist)
        artists = [i.find('a').text for i in artists]
        [print(f"{i}위 {j} : {k}")  # 디버깅
        for i, j, k in zip(range(1, len(titles)+1), titles, artists)]
        diction = {}  # dict 로 변환
        for i, j in enumerate(titles):
            diction[j] = artists[i]
        params[0].diction = diction
        params[0].dict_to_dataframe()
        params[0].dataframe_to_csv()  # csv파일로 저장

    def bugs_music(self, *params):    # BeautifulSoup 기본 크롤링
        soup = BeautifulSoup(urlopen(params[0].domain + params[0].query_string), 'lxml')
        title = {"class": params[0].class_names[0]}
        artist = {"class": params[0].class_names[1]}
        titles = soup.find_all(name=params[0].tag_name, attrs=title)
        titles = [i.find('a').text for i in titles]
        artists = soup.find_all(name=params[0].tag_name, attrs=artist)
        artists = [i.find('a').text for i in artists]
        [print(f"{i}위 {j} : {k}")  # 디버깅
        for i, j, k in zip(range(1, len(titles)+1), titles, artists)]
        diction = {}  # dict 로 변환
        for i, j in enumerate(titles):
            diction[j] = artists[i]
        params[0].diction = diction
        params[0].dict_to_dataframe()
        params[0].dataframe_to_csv()  # csv파일로 저장

    def naver_movie_review(self):
        if path.exists(r"C:\Users\AIA\PycharmProjects\django-react\DjangoServer\webcrawler\save\naver_movie_rank.csv") == True:
            rank = pd.read_csv(
                r"C:\Users\AIA\PycharmProjects\django-react\DjangoServer\webcrawler\save\naver_movie_rank.csv")
            result = [f'{i+1}위 : {j}' for i, j in enumerate(rank)]
            return result[0]
        else:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(driverpath)

            # Bluetooth: bluetooth_adapter_winrt.cc:1074 Getting Default Adapter failed error
            # https://darksharavim.tistory.com/606 → 해결
            # csv 있으면 arlet, 없으면 크롤링

            driver.get(naver_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            all_divs = soup.find_all('div', attrs={'class', 'tit3'})
            products = [[div.a.string for div in all_divs]]
            with open(f'{savepath}\\naver_movie_rank.csv', 'w', newline='', encoding=encoding) as f:
                wr = csv.writer(f)
                wr.writerows(products)
            driver.close()
            return "크롤링 완료"