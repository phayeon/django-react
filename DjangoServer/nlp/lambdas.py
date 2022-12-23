import random
import string
import datetime

lambda_string = lambda k: ''.join(random.sample(string.ascii_lowercase, k))
random_number = lambda start, end: random.randrange(start, end)
lambda_number = lambda k: ''.join(str(random_number(0, 10)) for i in range(k))
lambda_time = lambda x: datetime.datetime.now().strftime(x)

lambda_k_name = lambda fn, name: ''.join([fn[random_number(1, len(fn))], ''.join(name[random_number(1, len(name))] for i in range(random_number(1, 4)))])


if __name__ == '__main__':
    print(lambda_string(5))
    print(lambda_number(4))
    print(lambda_time('%Y-%m-%d %H:%M:%S'))
