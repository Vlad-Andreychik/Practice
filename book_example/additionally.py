# TODO[agorozhanko 14.10.2020]:нужно заменить print на logger
# TODO[vandreychyk 14.10.2020]: print на logger заменил
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('logs//additionally.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_error_details():
    return 2, 'описание ошибки №2'


def using_lambda():
    points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
    points.sort(key=lambda i: i['y'])
    logger.info(points)


def list_comprehension():
    list_one = [2, 3, 4]
    list_two = [2 * i for i in list_one if i > 2]
    logger.info(list_two)


def power_sum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    return total


def using_assert():
    my_list = ['item']
    assert len(my_list) >= 1
    print(my_list.pop())
    print(my_list)
    assert len(my_list) >= 1
