def count_it(digits):
    return {i: digits.count(i) for i in digits}


def max_dct(first_dict, second_dict):
    new_dict = {}
    a = ''
    for first_key in list(first_dict.keys()):
        for second_key in list(second_dict.keys()):
            if first_key == second_key:
                a += first_key
                if first_dict.get(first_key) >= second_dict.get(second_key):
                    new_dict[first_key] = first_dict.get(first_key)
                else:
                    new_dict[second_key] = second_dict.get(second_key)
            if second_key not in new_dict.keys():
                new_dict[second_key] = second_dict.get(second_key)
        if first_key not in new_dict.keys():
            new_dict[first_key] = first_dict.get(first_key)
    return new_dict


def three_max_keys(dictionary):
    list_dict = list(dictionary.items())
    list_dict.sort(key=lambda elem: elem[1], reverse=True)
    return dict(list_dict[:3])
