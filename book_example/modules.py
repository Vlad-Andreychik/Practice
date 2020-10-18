import logging
import sys
from math import sqrt

# TODO[agorozhanko 16.10.2020]: логер работает?
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('logs//modules.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def imp_sys():
    logger.info('Аргументы командной строки:')
    for i in sys.argv:
        logger.info(i)

    logger.info('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')
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
                    logger.info('%s простое' % a)
                    b = 1
                else:
                    pass
        if b != 1:
            logger.info('%s простое' % a)
            p = p + [a]
        count += 1
        a += 2
    logger.info('%s' % p)
    return p


def using_name():
    if __name__ == '__main__':
        logger.info('Эта программа запущена сама по себе.')
    else:
        logger.info('Меня импортировали в другой модуль.')
    return __name__


def say_hi():
    return 'Привет! Это говорит мой модуль.'


__version__ = '0.1'
