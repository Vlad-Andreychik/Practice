# TODO[agorozhanko 14.10.2020]:нужно заменить print на logger


def get_error_details():
    return 2, 'описание ошибки №2'


def using_lambda():
    points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
    points.sort(key=lambda i: i['y'])
    print(points)


def list_comprehension():
    # TODO[agorozhanko 14.10.2020]: название нужно исправить
    listone = [2, 3, 4]
    # TODO[agorozhanko 14.10.2020]: название нужно исправить
    listtwo = [2 * i for i in listone if i > 2]
    print(listtwo)


# TODO[agorozhanko 14.10.2020]: название нужно исправить
def powersum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    return total


def using_assert():
    # TODO[agorozhanko 14.10.2020]: название нужно исправить
    mylist = ['item']
    assert len(mylist) >= 1
    print(mylist.pop())
    print(mylist)
    assert len(mylist) >= 1
