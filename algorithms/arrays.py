import logging
from operator import itemgetter

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('..//logs//arrays.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def max_even_elem(array):
    """Принимает массив.

    Находит максимальный элемент с четным индексом.

    :param array: массив из чисел
    :type array: list
    :return: максимальный четный элемент массива
    :rtype: int
    """
    # Проверка на тип данных в массиве
    for elem in array:
        if not isinstance(elem, int):
            return logger.warning('Неверный ввод')
    # Проверка пустой ли массив
    try:
        maxi = array[0]
    except IndexError:
        return logger.warning('Введен пустой массив')

    for elem in array[::2]:
        if elem > maxi:
            maxi = elem
    return maxi


def swap_max_and_min(array):
    """Принимает массив.

    Меняет местами элементы с максимальным и
    минимальным значением.

    :param array: массив из чисел
    :type array: list
    :return: массив
    :rtype: list"""
    # Проверка на тип данных в массиве
    for elem in array:
        if not isinstance(elem, int):
            return logger.warning('Неверный ввод')
    # Проверка пустой ли массив
    try:
        maxi = array[0]
        mini = array[0]
    except IndexError:
        return logger.warning('Введен пустой массив')

    for elem in array:
        if elem > maxi:
            maxi = elem
        if elem < mini:
            mini = elem
    index_mini = array.index(mini)
    index_maxi = array.index(maxi)
    array[index_maxi] = mini
    array[index_mini] = maxi
    return array


def delete_negatives(array):
    """
    Дан массив целых чисел.

    Удаляет из него отрицательные значения.

    :param array: массив
    :type array: list
    :return: массив без отрицательных элементов
    :rtype: list
    """
    # Проверка на тип данных в массиве
    for elem in array:
        if not isinstance(elem, int):
            return logger.warning('Неверный ввод')
    # Проверка пустой ли массив
    try:
        array[0]
    except IndexError:
        return logger.warning('Введен пустой массив')

    negatives = []
    new_array = []
    for elem in array:
        if elem < 0:
            negatives.append(elem)
    for elem in array:
        if elem not in negatives:
            new_array.append(elem)
    return new_array


def selection_sort(array):
    """
    Дан массив чисел.

    Сортировка методом выборка по возрастанию

    :param array: массив из чисел
    :type array: list
    :return: отсортированный массив
    :rtype: list
    """
    # Проверка на тип данных в массиве
    for elem in array:
        if not isinstance(elem, int):
            return logger.warning('Неверный ввод')
    # Проверка пустой ли массив
    try:
        array[0]
    except IndexError:
        return logger.warning('Введен пустой массив')

    i = len(array)
    while i > 0:
        maxi = 0
        for number in range(1, i):
            if array[number] > array[maxi]:
                maxi = number
        array[maxi], array[i - 1] = array[i - 1], array[maxi]
        i -= 1
    return array


def frequency_sorting(array):
    """
        Дан массив чисел.

        Сортирует массив, расположив числа в порядке уменьшения их количества в списке.
        Если несколько чисел встречаются одинаково часто - их необходимо располагает в порядке от меньшего к большему.

        :param array: массив из чисел
        :type array: list
        :return: отсортированный массив
        :rtype: list
    """
    # Проверка на тип данных в массиве
    for elem in array:
        if not isinstance(elem, int):
            return logger.warning('Неверный ввод')
    # Проверка пустой ли массив
    try:
        array[0]
    except IndexError:
        return logger.warning('Введен пустой массив')

    array.sort()
    dictionary = {}
    new_array = []
    for num in array:
        dictionary[num] = array.count(num)
    numb = list(dictionary.items())
    numb = sorted(numb, key=itemgetter(1), reverse=True)
    for i in numb:
        for c in range(i[1]):
            new_array.append(i[0])
    return new_array
