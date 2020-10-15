# TODO[agorozhanko 14.10.2020]:нужно заменить print на logger


def shop():
    # TODO[agorozhanko 14.10.2020]: название нужно исправить
    # TODO[vandreychyk 15.10.2020]: название исправлено
    shop_list = ['яблоки', 'манго', 'морковь', 'бананы']

    print('Я должен сделать', len(shop_list), 'покупки: ')

    print('Покупки: ', end=' ')
    for item in shop_list:
        print(item, end=' ')

    print('\nТакже нужно купить риса.')
    shop_list.append('рис')
    print('Теперь мой список покупок таков: ', shop_list)

    print('Отсортирую-ка свой список')
    shop_list.sort()
    print('Отсортированный список покупок выглядит так: ', shop_list)

    print('Первое, что мне нужно купить, это', shop_list[0])
    # TODO[agorozhanko 14.10.2020]: название нужно исправить
    # TODO[vandreychyk 15.10.2020]: название исправлено
    old_item = shop_list[0]
    del shop_list[0]
    print('Я купил', old_item)
    print('Теперь мой список покупок: ', shop_list, '\n')
    return shop_list


def using_tuple():
    zoo = ('питон', 'слон', 'пингвин')
    print('Количество животных в зоопарке - ', len(zoo))

    new_zoo = 'обезьяна', 'верблюд', zoo
    print('Количество клеток в зоопарке -', len(new_zoo))
    print('Все животные в новом зоопарке: ', new_zoo)
    print('Животные, привезенные из старого зоопарка: ', new_zoo[2])
    print('Последнее животное, привезенное из старого зоопарка - ', new_zoo[2][2])
    print('Количество животных в новом зоопарке - ', len(new_zoo) - 1 +
          len(new_zoo[2]))
    return new_zoo


def using_dict():
    ab = {'Swaroop': 'swaroop@swaroopch.com',
          'Larry': 'larry@wall.org',
          'Matsumoto': 'matz@ruby-lang.org',
          'Spammer': 'spammer@hotmail.com'
          }

    print("Адрес Swaroop'a: ", ab['Swaroop'])

    del ab['Spammer']

    print('\nВ адресной книге {0} контакта\n'.format(len(ab)))

    for name, address in ab.items():
        print('Контакт {0} с адресом {1}'.format(name, address))

    ab['Guido'] = 'guido@python.org'

    if 'Guido' in ab:
        print('\nАдрес Guido: ', ab['Guido'])
    return ab


def seq():
    # TODO[agorozhanko 14.10.2020]: название нужно исправить
    # TODO[vandreychyk 15.10.2020]: название исправлено
    shop_list = ['яблоки', 'манго', 'морковь', 'бананы']
    name = 'swaroop'

    print('Элемент 0 -', shop_list[0])
    print('Элемент 1 -', shop_list[1])
    print('Элемент 2 -', shop_list[2])
    print('Элемент 3 -', shop_list[3])
    print('Элемент -1 -', shop_list[-1])
    print('Элемент -2 -', shop_list[-2])
    print('Символ 0 -', name[0])

    print('Элементы с 1 по 3:', shop_list[1:3])
    print('Элементы с 2 до конца:', shop_list[2:])
    print('Элементы с 1 по -1:', shop_list[1:-1])
    print('Элементы от начала до конца:', shop_list[:])

    print('Символы с 1 по 3:', name[1:3])
    print('Символы с 2 до конца:', name[2:])
    print('Символы с 1 до -1:', name[1:-1])
    print('Символы от начала до конца:', name[:])
    return shop_list


def reference():
    print('Простое присваивание')
    # TODO[agorozhanko 14.10.2020]: название нужно исправить
    # TODO[vandreychyk 15.10.2020]: название исправлено
    shop_list = ['яблоки', 'манго', 'морковь', 'бананы']
    # TODO[agorozhanko 14.10.2020]: название нужно исправить
    # TODO[vandreychyk 15.10.2020]: название исправлено
    my_list = shop_list

    del shop_list[0]

    print('shoplist:', shop_list)
    print('mylist:', my_list)

    print('Копирование при помощи полной вырезки')
    my_list = shop_list[:]
    del my_list[0]

    print('shoplist:', shop_list)
    print('mylist:', my_list)
    return my_list, shop_list


def str_methods():
    name = 'Swaroop'

    if name.startswith('Swa'):
        print('Да, строка начинается на "Swa"')

    if 'a' in name:
        print('Да, она содержит строку "a"')

    if name.find('war') != -1:
        print('Да, она содержит строку "war"')

    delimiter = '_*_'
    # TODO[agorozhanko 14.10.2020]: название нужно исправить
    # TODO[vandreychyk 15.10.2020]: название исправлено
    my_list = ['Бразилия', 'Россия', 'Индия', 'Китай']
    print(delimiter.join(my_list))
    return name, my_list
