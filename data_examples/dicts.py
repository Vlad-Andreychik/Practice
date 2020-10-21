keys = []  # Необходимо создание пустого списка и словаря для функции my_print
new_dict = {}


def count_it(digits):
    """Дана строка.

    Возвращает словарь, в котором ключи - элементы строки,
    а значения - количество этих элементов в данной строке"""
    return {i: digits.count(i) for i in digits}


def max_dct(first_dict, second_dict):
    """Дано два словаря.

    Создает третий словарь по правилу:
    Если в исходных словарях есть повторяющиеся ключи,
    выбираем среди двух с большим значением.
    Если ключ не повторяется,
    то просто переносим со своим значением в новый словарь.

    Возвращает словарь
    """
    third_dict = {}
    for first_key in list(first_dict.keys()):
        for second_key in list(second_dict.keys()):
            # Находим одинаковые ключи и добавляем в новый словарь этот ключ с наибольшим значением
            if first_key == second_key:
                if first_dict.get(first_key) >= second_dict.get(second_key):
                    third_dict[first_key] = first_dict.get(first_key)
                else:
                    third_dict[second_key] = second_dict.get(second_key)
            # Добавляем оставшиеся ключи в словарь
            if second_key not in third_dict.keys():
                third_dict[second_key] = second_dict.get(second_key)
        if first_key not in third_dict.keys():
            third_dict[first_key] = first_dict.get(first_key)
    return third_dict


def three_max_keys(dictionary):
    """Принимает словарь

    Сортирует его по значениям по убыванию

    Возвращает словарь с первыми тремя ключами отсортированного словаря"""
    list_dict = list(dictionary.items())
    list_dict.sort(key=lambda elem: elem[1], reverse=True)
    return dict(list_dict[:3])


def my_print(dictionary):
    """Дан словарь.

    Необходимо сделать этот словарь "плоским",
    но сохранить структуру в ключах.
    Результатом будет словарь без вложенных словарей.
    Ключи должны содержать путь,
    составленный из родительских ключей из начального словаря,
    разделенных "/".

    Возвращает словарь"""
    for k, v in dictionary.items():
        if isinstance(v, dict):
            keys.append(k)
            my_print(v)
        else:
            keys.append(k)
            new_key = '/'.join(keys)
            new_dict[new_key] = v
    return new_dict


def multiple_values(dictionary):
    """Дан словарь со значениями в виде чисел.

    Возвращает произведение значений"""
    result = 1
    for key in dictionary:
        result *= dictionary[key]
    return result
