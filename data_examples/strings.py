import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('..//logs//string.logs', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def reverse(text):
    """Принимает строку

    Возвращает обратную строку"""
    return text[::-1]


def unrepeated_letters(text):
    """Принимает строку

    Возвращает строку без повторения букв"""
    word = ''
    for i in text:
        letter = i
        if letter not in word and letter != ' ':
            word += letter
    return word


def count_words(text):
    """Принимает строку

    Возвращает количество слов в строке"""
    return len(text.split())


def change_piece(text, old, new):
    """Принимает строку, заменяемый кусок, новый кусок.

    Замена старого куска строки на новый.

    Возвращает новую строку"""
    i = text.find(old)
    size = len(text)
    word = text[0:i] + new
    if i != -1 and i != size - 1:
        word += text[i + len(old):]
    return word


def sum_numbers(text):
    """Принимает строку

    Возвращает сумму чисел, находящихся в строке"""
    # Суммирую все цифры
    num = 0
    for number in text:
        if number.isdigit():
            num += int(number)
    # Создаю из строки список по разделителю '-'.
    # Первая цифра любого элемента списка, кроме первого, - отрицательное число
    text_split = text.split('-')
    try:
        if text_split[0][0].isdigit():
            del text_split[0]
    except IndexError:
        pass
    # Отнимаю удвоенное значение цифры, так как до этого я эту же цифру прибавлял
    for i in text_split:
        try:
            if i[0].isdigit():
                num -= int(i[0]) * 2
        except IndexError:
            continue
    return num


def reverse_words_positions(text):
    """Принимает строку

    Возвращает строку с обратным порядком слов"""
    return ' '.join(text.split()[::-1])


def delete_spaces(text):
    """Принимает строку

    Удаление лишних пробелов в начале, в конце строки,
     а также между словами

     Возвращает строку"""
    return ' '.join(text.strip(' ').split())
