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
    print('Теперь мой список покупок: ', shoplist)


def tuple():
    zoo = ('питон', 'слон', 'пингвин')
    print('Количество животных в зоопарке - ', len(zoo))

    new_zoo = 'обезьяна', 'верблюд', zoo
    print('Количество клеток в зоопарке -', len(new_zoo))
    print('Все животные в новом зоопарке: ', new_zoo)
    print('Животные, привезенные из старого зоопарка: ', new_zoo[2])
    print('Последнее животное, привезенное из старого зоопарка - ', new_zoo[2][2])
    print('Количество животных в новом зоопарке - ', len(new_zoo) - 1 + \
          len(new_zoo[2]))


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