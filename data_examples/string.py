import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('logs//string.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def reverse(text):
    return text[::-1]


def unrepeated_letters(text):
    word = ''
    for i in text:
        letter = i
        if letter not in word and letter != ' ':
            word += letter
    return word


def count_words(text):
    text = text.split()
    return len(text)


def change_piece(text, old, new):
    i = text.find(old)
    text = text[0:i] + new + text[i + len(old):]
    return text


def sum_numbers(text):
    num = 0
    for number in text:
        try:
            if number.isdigit():
                num += int(number)
        except ValueError:
            continue
    return num


def reverse_words_positions(text):
    return ' '.join(text.split()[::-1])


def delete_spaces(text):
    return ' '.join(text.strip(' ').split())
