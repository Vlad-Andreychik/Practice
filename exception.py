import time


def try_except():
    try:
        text = input('Введите что-нибудь --> ')
    except EOFError:
        print('Ну зачем вы сделали мне EOF?')
    except KeyboardInterrupt:
        print('Вы отменили операцию.')
    else:
        print('Вы ввели {0}'.format(text))


def final():
    try:
        f = open('poem.txt')
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            print(line, end='')
            time.sleep(2)
    except KeyboardInterrupt:
        print('!! Вы отменили чтение файла.')

    finally:
        f.close()
        print('(Очистка: Закрытие файла)')


class ShortInputException(Exception):
    '''Пользовательский класс исключения.'''

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


def with_with():
    with open('poem.txt') as f:
        for line in f:
            print(line, end='')