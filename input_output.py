import logging
import pickle

logger = logging.getLogger(__name__)


# TODO[agorozhanko 14.10.2020]:нужно заменить print на logger
# TODO[vandreychyk 15.10.2020]: заменил

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
        logger.info(line, end='')
    f.close()


def pickling():
    # TODO[agorozhanko 14.10.2020]: название нужно исправить
    # TODO[vandreychyk 15.10.2020]: название исправлено
    shop_list_file = 'shop_list.data'
    # TODO[agorozhanko 14.10.2020]: название нужно исправить
    # TODO[vandreychyk 15.10.2020]: название исправлено
    shop_list = ['яблоки', 'манго', 'морковь']

    f = open(shop_list_file, 'wb')
    pickle.dump(shop_list, f)
    f.close()
    del shop_list
