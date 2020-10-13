def shop():
    shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

    print('Я должен сделать', len(shoplist), 'покупки: ')

    print('Покупки: ', end=' ')
    for item in shoplist:
        print(item, end=' ')

    print('\nТакже нужно купить риса.')
    shoplist.append('рис')
    print('Теперь мой список покупок таков: ', shoplist)

    print('Отсортирую-ка свой список')
    shoplist.sort()
    print('Отсортированный список покупок выглядит так: ', shoplist)

    print('Первое, что мне нужно купить, это', shoplist[0])
    olditem = shoplist[0]
    del shoplist[0]
    print('Я купил', olditem)
    print('Теперь мой список покупок: ', shoplist, '\n')
    return shoplist


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
    shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
    name = 'swaroop'

    print('Элемент 0 -', shoplist[0])
    print('Элемент 1 -', shoplist[1])
    print('Элемент 2 -', shoplist[2])
    print('Элемент 3 -', shoplist[3])
    print('Элемент -1 -', shoplist[-1])
    print('Элемент -2 -', shoplist[-2])
    print('Символ 0 -', name[0])

    print('Элементы с 1 по 3:', shoplist[1:3])
    print('Элементы с 2 до конца:', shoplist[2:])
    print('Элементы с 1 по -1:', shoplist[1:-1])
    print('Элементы от начала до конца:', shoplist[:])

    print('Символы с 1 по 3:', name[1:3])
    print('Символы с 2 до конца:', name[2:])
    print('Символы с 1 до -1:', name[1:-1])
    print('Символы от начала до конца:', name[:])
    return shoplist


def reference():
    print('Простое присваивание')
    shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
    mylist = shoplist

    del shoplist[0]

    print('shoplist:', shoplist)
    print('mylist:', mylist)

    print('Копирование при помощи полной вырезки')
    mylist = shoplist[:]
    del mylist[0]

    print('shoplist:', shoplist)
    print('mylist:', mylist)


def str_methods():
    name = 'Swaroop'

    if name.startswith('Swa'):
        print('Да, строка начинается на "Swa"')

    if 'a' in name:
        print('Да, она содержит строку "a"')

    if name.find('war') != -1:
        print('Да, она содержит строку "war"')

    delimiter = '_*_'
    mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
    print(delimiter.join(mylist))
