import logging

# TODO[agorozhanko 14.10.2020]:нужно заменить print на logger
# TODO[vandreychyk 15.10.2020]: заменил
# TODO[agorozhanko 16.10.2020]: вижу функцию print
logger = logging.getLogger(__name__)


def shop():
    shop_list = ['яблоки', 'манго', 'морковь', 'бананы']

    logger.info('Я должен сделать', len(shop_list), 'покупки: ')

    logger.info('Покупки: ', end=' ')
    for item in shop_list:
        print(item, end=' ')

    logger.info('\nТакже нужно купить риса.')
    shop_list.append('рис')
    logger.info('Теперь мой список покупок таков: ', shop_list)

    logger.info('Отсортирую-ка свой список')
    shop_list.sort()
    logger.info('Отсортированный список покупок выглядит так: ', shop_list)

    logger.info('Первое, что мне нужно купить, это', shop_list[0])
    old_item = shop_list[0]
    del shop_list[0]
    logger.info('Я купил', old_item)
    logger.info('Теперь мой список покупок: ', shop_list, '\n')
    return shop_list


def using_tuple():
    zoo = ('питон', 'слон', 'пингвин')
    logger.info('Количество животных в зоопарке - ', len(zoo))

    new_zoo = 'обезьяна', 'верблюд', zoo
    logger.info('Количество клеток в зоопарке -', len(new_zoo))
    logger.info('Все животные в новом зоопарке: ', new_zoo)
    logger.info('Животные, привезенные из старого зоопарка: ', new_zoo[2])
    logger.info('Последнее животное, привезенное из старого зоопарка - ', new_zoo[2][2])
    logger.info('Количество животных в новом зоопарке - ', len(new_zoo) - 1 +
                len(new_zoo[2]))
    return new_zoo


def using_dict():
    ab = {'Swaroop': 'swaroop@swaroopch.com',
          'Larry': 'larry@wall.org',
          'Matsumoto': 'matz@ruby-lang.org',
          'Spammer': 'spammer@hotmail.com'
          }

    logger.info("Адрес Swaroop'a: ", ab['Swaroop'])

    del ab['Spammer']

    logger.info('\nВ адресной книге {0} контакта\n'.format(len(ab)))

    for name, address in ab.items():
        logger.info('Контакт {0} с адресом {1}'.format(name, address))

    ab['Guido'] = 'guido@python.org'

    if 'Guido' in ab:
        logger.info('\nАдрес Guido: ', ab['Guido'])
    return ab


def seq():
    shop_list = ['яблоки', 'манго', 'морковь', 'бананы']
    name = 'swaroop'

    logger.info('Элемент 0 -', shop_list[0])
    logger.info('Элемент 1 -', shop_list[1])
    logger.info('Элемент 2 -', shop_list[2])
    logger.info('Элемент 3 -', shop_list[3])
    logger.info('Элемент -1 -', shop_list[-1])
    logger.info('Элемент -2 -', shop_list[-2])
    logger.info('Символ 0 -', name[0])

    logger.info('Элементы с 1 по 3:', shop_list[1:3])
    logger.info('Элементы с 2 до конца:', shop_list[2:])
    logger.info('Элементы с 1 по -1:', shop_list[1:-1])
    logger.info('Элементы от начала до конца:', shop_list[:])

    logger.info('Символы с 1 по 3:', name[1:3])
    logger.info('Символы с 2 до конца:', name[2:])
    logger.info('Символы с 1 до -1:', name[1:-1])
    logger.info('Символы от начала до конца:', name[:])
    return shop_list


def reference():
    print('Простое присваивание')
    shop_list = ['яблоки', 'манго', 'морковь', 'бананы']
    my_list = shop_list

    del shop_list[0]

    logger.info('shoplist:', shop_list)
    logger.info('mylist:', my_list)

    logger.info('Копирование при помощи полной вырезки')
    my_list = shop_list[:]
    del my_list[0]

    logger.info('shoplist:', shop_list)
    logger.info('mylist:', my_list)
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
