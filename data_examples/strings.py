import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('logs//string.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def reverse(text):
    """Возвращает обратную строку"""
    return text[::-1]


def unrepeated_letters(text):
    """Возвращает строку без повторения букв"""
    word = ''
    for i in text:
        letter = i
        if letter not in word and letter != ' ':
            word += letter
    return word


def count_words(text):
    """Возвращает количество слов в строке"""
    return len(text.split())


def change_piece(text, old, new):
    """Замена куска строки.

    Возвращает новую строку с замененным куском"""
    i = text.find(old)
    size = len(text)
    word = text[0:i] + new
    if i != -1 and i != size - 1:
        word += text[i + len(old):]
    return word


def sum_numbers(text):
    """Возвращает сумму чисел, находящихся в строке"""
    num = 0
    for number in text:
        try:
            if number.isdigit():
                num += int(number)
        except ValueError:
            continue
    return num


def reverse_words_positions(text):
    """Возвращает строку с обратным порядком слов"""
    return ' '.join(text.split()[::-1])


def delete_spaces(text):
    """Удаление лишних пробелов в начале, в конце строки,
     а также между словами"""
    return ' '.join(text.strip(' ').split())
