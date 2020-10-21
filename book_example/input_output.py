import logging
import pickle

# TODO[agorozhanko 16.10.2020]: логер работает?
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('logs//input_output.logs', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def user_input():
    def reverse(text):
        return text[::-1]

    def is_palindrome(text):
        return text == reverse(text)

    something = input('Введите текст: ')
    if is_palindrome(something):
        logger.info('Да, это палиндром')
    else:
        logger.info('Нет, это не палиндром')


def using_file():
    poem = '''\
    Программировать весело.
    Если работа скучна,
    Чтобы придать ей весёлый тон -
    используй Python!
    '''
    f = open('poem.txt', 'w')
    f.write(poem)
    f.close()
    f = open('poem.txt')

    while True:
        line = f.readline()
        if len(line) == 0:
            break
        logger.info(line)
    f.close()
    return poem, line


def pickling():
    shop_list_file = 'shop_list.data'
    shop_list = ['яблоки', 'манго', 'морковь']

    f = open(shop_list_file, 'wb')
    pickle.dump(shop_list, f)
    f.close()
    del shop_list
