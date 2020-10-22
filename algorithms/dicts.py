def count_it(text):
    """Дана строка.

    Возвращает словарь, в котором ключи - элементы строки,
    а значения - количество этих элементов в данной строке
    :param text: строка
    :type text: str
    :return: Словарь
    :rtype: dict"""
    return {i: text.count(i) for i in text}


def max_dct(first_dict, second_dict):
    """Дано два словаря.

    Создает третий словарь по правилу:
    Если в исходных словарях есть повторяющиеся ключи,
    выбираем среди двух с большим значением.
    Если ключ не повторяется,
    то просто переносим со своим значением в новый словарь.

    Возвращает словарь
    :param first_dict: Первый словарь
    :type first_dict: dict
    :param second_dict: Второй словарь
    :type second_dict: dict
    :return: новый словарь
    :rtype: dict
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

    Сортирует его по значениям по убыванию.
    При введении значений типа отличного от int будет возвращаться пустой словарь.

    Возвращает словарь с первыми тремя ключами отсортированного словаря
    :param dictionary: словарь
    :type dictionary: dict
    :return: словарь с тремя ключами с наибольшим значением
    :rtype: dict
    """
    flag = True
    for value in dictionary.values():
        if isinstance(value, int):
            flag = True
        else:
            flag = False
            break
    if flag:
        list_dict = list(dictionary.items())
        list_dict.sort(key=lambda elem: elem[1], reverse=True)
        return dict(list_dict[:3])
    else:
        return {}


def my_print(dictionary):
    """Дан словарь.

    Необходимо сделать этот словарь "плоским",
    но сохранить структуру в ключах.
    Результатом будет словарь без вложенных словарей.
    Ключи должны содержать путь,
    составленный из родительских ключей из начального словаря,
    разделенных "/".

    Возвращает словарь
    :param dictionary: словарь, возможно с вложенными словарями
    :type dictionary: dict
    :return: словарь без вложенных словарей
    :rtype: dict
    """
    new_dict = {}
    for key, value in dictionary.items():
        if not isinstance(value, dict) or (not value):
            new_dict[key] = value or ''
        else:
            for suffix, n_value in my_print(value).items():
                r_key = key + '/' + suffix
                new_dict[r_key] = n_value
    return new_dict


def multiple_values(dictionary):
    """Дан словарь со значениями в виде чисел.

    Возвращает произведение значений.
    При введении значений типа отличного от int будет возвращаться 0.
    :param dictionary: словарь
    :type dictionary: dict
    :return: произведение значений словаря
    :rtype: int
    """
    flag = False
    for value in dictionary.values():
        if isinstance(value, int):
            flag = True
        else:
            flag = False
            break
    if flag:
        result = 1
        for key in dictionary:
            result *= dictionary[key]
        return result
    else:
        return 0
