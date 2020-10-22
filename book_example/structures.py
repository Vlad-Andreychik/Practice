import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
# TODO[agorozhanko 21.10.2020]: не правильное рассширение у файла лога
# TODO[vandreychyk 22.10.2020]: исправил
file_handler = logging.FileHandler('..//logs//structures.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def shop():
    shop_list = ['яблоки', 'манго', 'морковь', 'бананы']

    logger.info('Я должен сделать %s покупки: ' % len(shop_list))

    logger.info('Покупки: ')
    for item in shop_list:
        logger.info('%s' % item)

    logger.info('Также нужно купить риса.')
    shop_list.append('рис')
    logger.info('Теперь мой список покупок таков: %s' % shop_list)

    logger.info('Отсортирую-ка свой список')
    shop_list.sort()
    logger.info('Отсортированный список покупок выглядит так: %s' % shop_list)

    logger.info('Первое, что мне нужно купить, это %s' % shop_list[0])
    old_item = shop_list[0]
    del shop_list[0]
    logger.info('Я купил %s' % old_item)
    logger.info('Теперь мой список покупок: %s' % shop_list)
    return shop_list


def using_tuple():
    zoo = ('питон', 'слон', 'пингвин')
    logger.info('Количество животных в зоопарке - %s' % len(zoo))

    new_zoo = 'обезьяна', 'верблюд', zoo
    logger.info('Количество клеток в зоопарке - %s' % len(zoo))
    logger.info('Все животные в новом зоопарке: %s%s%s' % new_zoo)
    logger.info('Животные, привезенные из старого зоопарка: %s%s%s' % new_zoo[2])
    logger.info('Последнее животное, привезенное из старого зоопарка - %s' % new_zoo[2][2])
    logger.info('Количество животных в новом зоопарке - %s' % (len(new_zoo) - 1 +
                                                               len(new_zoo[2])))
    return new_zoo


def using_dict():
    ab = {'Swaroop': 'swaroop@swaroopch.com',
          'Larry': 'larry@wall.org',
          'Matsumoto': 'matz@ruby-lang.org',
          'Spammer': 'spammer@hotmail.com'
          }

    logger.info("Адрес Swaroop'a: %s" % ab['Swaroop'])

    del ab['Spammer']

    logger.info('В адресной книге %s контакта' % len(ab))

    for name, address in ab.items():
        logger.info('Контакт %s с адресом %s' % (name, address))

    ab['Guido'] = 'guido@python.org'

    if 'Guido' in ab:
        logger.info('Адрес Guido: %s' % ab['Guido'])
    return ab


def seq():
    shop_list = ['яблоки', 'манго', 'морковь', 'бананы']
    name = 'swaroop'

    logger.info('Элемент 0 - %s' % shop_list[0])
    logger.info('Элемент 1 - %s' % shop_list[1])
    logger.info('Элемент 2 - %s' % shop_list[2])
    logger.info('Элемент 3 - %s' % shop_list[3])
    logger.info('Элемент -1 - %s' % shop_list[-1])
    logger.info('Элемент -2 - %s' % shop_list[-2])
    logger.info('Символ 0 - %s' % name[0])

    logger.info('Элементы с 1 по 3: %s' % shop_list[1:3])
    logger.info('Элементы с 2 до конца: %s' % shop_list[2:])
    logger.info('Элементы с 1 по -1: %s' % shop_list[1:-1])
    logger.info('Элементы от начала до конца: %s' % shop_list[:])

    logger.info('Символы с 1 по 3: %s' % name[1:3])
    logger.info('Символы с 2 до конца: %s' % name[2:])
    logger.info('Символы с 1 до -1: %s' % name[1:-1])
    logger.info('Символы от начала до конца: %s' % name[:])
    return shop_list


def reference():
    logger.info('Простое присваивание')
    shop_list = ['яблоки', 'манго', 'морковь', 'бананы']
    my_list = shop_list

    del shop_list[0]

    logger.info('shop_list: %s' % shop_list)
    logger.info('my_list: %s' % my_list)

    logger.info('Копирование при помощи полной вырезки')
    my_list = shop_list[:]
    del my_list[0]

    logger.info('shop_list: %s' % shop_list)
    logger.info('my_list: %s' % my_list)
    return my_list, shop_list


def str_methods():
    name = 'Swaroop'

    if name.startswith('Swa'):
        logger.info('Да, строка начинается на "Swa"')

    if 'a' in name:
        logger.info('Да, она содержит строку "a"')

    if name.find('war') != -1:
        logger.info('Да, она содержит строку "war"')

    delimiter = '_*_'
    my_list = ['Бразилия', 'Россия', 'Индия', 'Китай']
    logger.info(delimiter.join(my_list))
    return name, my_list
