import sys
from math import sqrt


def imp_sys():
    print('Аргументы командной строки:')
    for i in sys.argv:
        print(i)

    print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')
    return sys.path


def simple_or_not(n):
    p = [2, 3]
    count = 2
    a = 5
    while count < n:
        b = 0
        for i in range(2, a):
            if i <= sqrt(a):
                if a % i == 0:
                    print(a, 'непростое')
                    b = 1
                else:
                    pass
        if b != 1:
            print(a, 'простое')
            p = p + [a]
        count += 1
        a += 2
    print(p)
    return p


def using_name():
    if __name__ == '__main__':
        print('Эта программа запущена сама по себе.')
    else:
        print('Меня импортировали в другой модуль.')
    return __name__


def sayhi():
    return 'Привет! Это говорит мой модуль.'


__version__ = '0.1'
