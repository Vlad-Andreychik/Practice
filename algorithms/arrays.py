def max_even_elem(array):
    """Принимает массив.

    Возвращает максимальный элемент с четным индексом"""
    maxi = array[0]
    for elem in array[::2]:
        if elem > maxi:
            maxi = elem
    return maxi


def swap_max_and_min(array):
    """Принимает массив.

    Меняет местами элементы с максимальным и
    минимальным значением

    Возвращает массив"""
    maxi = array[0]
    mini = array[0]
    for elem in array:
        if elem > maxi:
            maxi = elem
        if elem < mini:
            mini = elem
    temp = array[array.index(mini)]
    array[array.index(mini)] = array[array.index(maxi)]
    array[array.index(maxi)] = temp
    return array
