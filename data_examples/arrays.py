def max_even_elem(a):
    """Возвращает максимальный элемент с четным индексом"""
    maxi = a[0]
    for elem in a[::2]:
        if elem > maxi:
            maxi = elem
    return maxi
