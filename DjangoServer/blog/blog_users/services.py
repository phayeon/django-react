import random
import string

import pandas as pd
from sqlalchemy import create_engine


class UserService(object):
    def __init__(self):
        pass

    def creat_users(self):
        user_info = [{'email': ''.join([(''.join(random.choices(string.ascii_lowercase, k=5))), '@gmail.com']),
                  'nickname': ''.join(random.choices(string.ascii_lowercase, k=5)),
                  'password': 'qwe123'} for i in range(100)]

        df = pd.DataFrame(user_info)

        # conda install -c anaconda sqlalchemy
        # conda install pymysql

        engine = create_engine(
            "mysql+pymysql://root:root@localhost:3306/mydb",
            encoding='utf-8')

        # pip install sqlalchemy==1.4.0

        df.to_sql(name='blog_user',
                  if_exists='append', # append 계속 쓰면 쌓인다. 적당히 써라.
                  con=engine,
                  index=False)

        print(user_info)
        return user_info

        # 쿼리문으로 테이블 '데이터'만 삭제하기
        # 테이블 삭제하면 다시 만들어야 해서 귀찮아짐


if __name__ == '__main__':
    UserService().creat_users()