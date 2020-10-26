import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('..//logs//tuples.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def above_average(tupl):
    """
    Принимает кортеж, в котором каждый элемент содержит имя и возраст.
    Возвращает кортеж с элементами, чей возраст выше среднего.
    :param tupl: кортеж
    :return: кортеж
    """
    average = 0
    list_above_average = []
    try:
        for i in tupl:
            average += int(i.split()[1])
        for i in tupl:
            if int(i.split()[1]) > average / len(tupl):
                list_above_average.append(i)
    except IndexError:
        logger.warning('Неправильный ввод')
    return tuple(list_above_average)


def union_tuples(first_tuple, second_tuple):
    """
    Принимает два кортежа. Создает третий кортеж путем объединения первых двух.
    Возвращает третий кортеж и количество нулей в нем
    :param first_tuple: кортеж
    :param second_tuple: кортеж
    :return: кортеж, число
    """
    new_tuple = []
    try:
        list_first_tuple = list(first_tuple)
        list_second_tuple = list(second_tuple)
        new_tuple = list_first_tuple + list_second_tuple
    except IndexError:
        logger.warning('Неправильный ввод')
    return tuple(new_tuple), new_tuple.count(0)
