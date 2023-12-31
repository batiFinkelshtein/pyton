# This is a sample Python script.

import datetime
from functools import lru_cache
from timeit import repeat


def Mytime(func):
    def func1(*args,**kwargs):
        time1 = datetime.datetime.now()
        func(*args)
        time2 = datetime.datetime.now()
        print(time2 - time1)

    return func1


cache1 = dict()


def cache(func):
    def wrapper(*args, **kwargs):
        if args[0]  not in cache1:
            cache1[args[0]]=func(*args)
        return cache1[args[0]]
    return wrapper



@Mytime
@cache
def Fibonacci(n,ret=[], i=0,count=1, num1=0, num2=1, next_number=1):
    while count <= n:
        ret.append(next_number)
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    return ret


@Mytime
def Myprint():
    for i in range(100000000):
        i * 100000


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Myprint()
    Fibonacci(1000)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
