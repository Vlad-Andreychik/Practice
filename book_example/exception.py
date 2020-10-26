import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('..//logs//exception.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def try_except():
    try:
        text = input('Введите что-нибудь --> ')
    except EOFError:
        logger.info('Ну зачем вы сделали мне EOF?')
    except KeyboardInterrupt:
        logger.info('Вы отменили операцию.')
    else:
        logger.info('Вы ввели {0}'.format(text))


def final():
    try:
        f = open('poem.txt')
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            logger.info(line, end='')
            time.sleep(2)
    except KeyboardInterrupt:
        logger.info('!! Вы отменили чтение файла.')

    finally:
        f.close()
        logger.info('(Очистка: Закрытие файла)')


class ShortInputException(Exception):
    '''Пользовательский класс исключения.'''

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


def with_with():
    with open('poem.txt') as f:
        for line in f:
            logger.info(line, end='')
