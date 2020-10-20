def max_even_elem(a):
    """Возвращает максимальный элемент с четным индексом"""
    maxi = a[0]
    for elem in a[::2]:
        if elem > maxi:
            maxi = elem
    return maxi


def swap_max_and_min(a):
    """Меняет местами элементы с максимальным и
     минимальным значением"""
    maxi = a[0]
    mini = a[0]
    for elem in a:
        if elem > maxi:
            maxi = elem
        if elem < mini:
            mini = elem
    temp = a[a.index(mini)]
    a[a.index(mini)] = a[a.index(maxi)]
    a[a.index(maxi)] = temp
    return a
