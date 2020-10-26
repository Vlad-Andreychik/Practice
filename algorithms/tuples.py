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
    :type tupl: tuple
    :return: кортеж
    :rtype: tuple
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
    :type first_tuple: tuple
    :param second_tuple: кортеж
    :type second_tuple: tuple
    :return: кортеж
    :rtype: tuple
    """
    new_tuple = []
    try:
        list_first_tuple = list(first_tuple)
        list_second_tuple = list(second_tuple)
        new_tuple = list_first_tuple + list_second_tuple
    except IndexError:
        logger.warning('Неправильный ввод')
    return tuple(new_tuple), new_tuple.count(0)


def slicer(tupl, element):
    """
    Принимает кортеж и случайный элемент. Возвращает новый кортеж,
    начинающийся с первого появления элемента в нем и
    заканчивающийся вторым его появлением включительно.
    Если элемента нет вовсе – вернуть пустой кортеж.

    :param tupl: кортеж
    :type tupl: tuple
    :param element: элемент
    :type element: Any
    :return: кортеж
    :rtype:tuple
    """
    try:
        if tupl.count(element) > 1:
            tupl_1 = tupl[tupl.index(element) + 1:]
            return tupl[tupl.index(element):tupl.index(element) + tupl_1.index(element) + 2]
        elif tupl.count(element) == 1:
            return tupl[tupl.index(element):]
        else:
            return ()
    except ValueError:
        logger.warning('Неправильный ввод')
    except TypeError:
        logger.warning('Неправильный ввод')


def sieve(list_of_integers):
    """
    На вход поступает список целых чисел.
    В результате выполнения этой функции будет получен кортеж
    уникальных элементов списка в обратном порядке.

    :param list_of_integers: список целых чисел
    :type list_of_integers: list
    :return: кортеж
    :rtype: tuple
    """
    try:
        for i in list_of_integers:
            if not isinstance(i, int):
                raise ValueError
        set_of_list = set(list_of_integers)
        return tuple(sorted(set_of_list))
    except (ValueError, TypeError):
        logger.warning('Неправильный ввод')


def del_from_tuple(tupl, element):
    """
    На вход поступает кортеж и элемент.
    Функция удаляет первое появление определенного элемента из кортежа по значению
    и возвращать кортеж без оного.

     :param tupl: кортеж
     :type tupl: tuple
     :param element: элемент
     :type element: Any
     :return: кортеж
     :rtype: tuple
     """
    try:
        if element not in tupl:
            return tupl
        list_of_tuple = list(tupl)
        list_of_tuple.remove(element)
        return tuple(list_of_tuple)
    except (ValueError, TypeError):
        logger.warning('Неправильный ввод')
