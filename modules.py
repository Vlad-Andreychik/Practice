import sys
from math import sqrt


def imp_sys():
    print('Аргументы командной строки:')
    for i in sys.argv:
        print(i)

    print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')


def simple_or_not():
    n = int(input("Введите диапазон:- "))
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
