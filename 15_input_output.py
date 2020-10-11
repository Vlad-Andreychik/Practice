import pickle


def user_input():
    def reverse(text):
        return text[::-1]

    def is_palindrome(text):
        return text == reverse(text)

    something = input('Введите текст: ')
    if is_palindrome(something):
        print('Да, это палиндром')
    else:
        print('Нет, это не палиндром')


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
        print(line, end='')
    f.close()


def pickling():
    shoplistfile = 'shoplist.data'

    shoplist = ['яблоки', 'манго', 'морковь']

    f = open(shoplistfile, 'wb')
    pickle.dump(shoplist, f)
    f.close()
    del shoplist
