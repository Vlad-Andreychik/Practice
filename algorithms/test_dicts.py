from algorithms import dicts


def test_count_it_empty():
    """Проверка пустого ввода"""
    assert (dicts.count_it('')) == {}


def test_count_it_letters():
    """Проверка строки из букв"""
    assert (dicts.count_it('abcdab')) == {'a': 2, 'b': 2, 'c': 1, 'd': 1}


def test_count_it_numbers():
    """Проверка строки из цифр"""
    assert (dicts.count_it('1234534')) == {'1': 1, '2': 1, '3': 2, '4': 2, '5': 1}


def test_count_it_symbols():
    """Проверка строки из спецсимволов"""
    assert (dicts.count_it('/&@%;%$+')) == {'$': 1, '%': 2, '&': 1, '+': 1, '/': 1, ';': 1, '@': 1}


def test_count_it_sentence():
    """Проверка строку из нескольких слов"""
    assert (dicts.count_it('Hello world')) == {' ': 1, 'H': 1, 'd': 1, 'e': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1}


def test_max_dct_both_empty():
    """Вводим пустые словари"""
    assert (dicts.max_dct({}, {})) == {}


def test_max_dct_one_empty():
    """Вводим один пустой словарь, один заполненный"""
    assert (dicts.max_dct({}, {'a': 1, 'b': 2, 'c': 3})) == {}


def test_max_dct_normal_input():
    """Вводим два заполненных словаря, у которых есть одинаковые ключи"""
    assert (dicts.max_dct({'a': 2, 'b': 2, 'c': 1, 'd': 1}, {'a': 1, 'b': 2, 'c': 3})) == {'a': 2, 'b': 2, 'c': 3,
                                                                                           'd': 1}


def test_max_dct_different_keys():
    """Вводим два заполненных словаря, у которых нет одинаковых ключей"""
    assert (dicts.max_dct({'f': 2, 'q': 1, 'd': 1}, {'a': 1, 'b': 2, 'c': 3})) == {'f': 2, 'q': 1, 'd': 1, 'a': 1,
                                                                                   'b': 2, 'c': 3}


def test_max_dct_with_negative_values():
    """Вводим два заполненных словаря, у которых есть отрицательные значения"""
    assert (dicts.max_dct({'a': 2, 'b': 2, 'c': 1, 'd': -5}, {'a': -7, 'b': 2, 'c': 3})) == {'a': 2, 'b': 2, 'c': 3,
                                                                                             'd': -5}


def test_three_max_keys_empty():
    """Вводим пустой словарь"""
    assert (dicts.three_max_keys({})) == {}


def test_three_max_keys_with_different_type_of_values():
    """Вводим словарь со значениями разных типов"""
    assert (dicts.three_max_keys({'a': 2, 'b': '2', 'c': True, 'd': -5})) == {}


def test_three_max_keys_with_2_keys():
    """Вводим словарь с двумя ключами"""
    assert (dicts.three_max_keys({'a': 2, 'b': 2})) == {'a': 2, 'b': 2}


def test_three_max_keys_with_3_keys():
    """Вводим словарь с тремя ключами"""
    assert (dicts.three_max_keys({'a': 2, 'b': 2, 'c': 3})) == {'a': 2, 'b': 2, 'c': 3}


def test_three_max_keys_with_4_keys():
    """Вводим словарь с четырьмя ключами"""
    assert (dicts.three_max_keys({'a': 2, 'b': 2, 'c': 1, 'd': -5})) == {'a': 2, 'b': 2, 'c': 1}


def test_my_print_empty():
    """Вводим пустой словарь"""
    assert (dicts.my_print({})) == {}


def test_my_print_without_nested_dictionaries():
    """Вводим словарь без вложенных в него словарей"""
    assert (dicts.my_print({'a': 1, 'b': 2, 'c': 3})) == {'a': 1, 'b': 2, 'c': 3}


def test_my_print_with_one_nested_dictionary():
    """Вводим словарь с одним вложенным словарем"""
    assert (dicts.my_print({"name": {"first": "One"}, "job": "scout"})) == {'job': 'scout', 'name/first': 'One'}


def test_my_print_with_couple_nested_dictionaries():
    """Вводим словарь с несколькими вложенными словарями"""
    assert (dicts.my_print({"name": {"first": "One", "last": "Drone"}, "job": "scout", "recent": {},
                            "additional": {"place": {"zone": "1", "cell": "2"}}})) == {"name/first": "One",
                                                                                       "name/last": "Drone",
                                                                                       "job": "scout", "recent": "",
                                                                                       "additional/place/zone": "1",
                                                                                       "additional/place/cell": "2"}


def test_my_print_with_different_type_of_values():
    """Вводим словарь со значениями разных типов"""
    assert (dicts.my_print({"name": {"first": "One", "last": "Drone"}, "job": "scout", "recent": {},
                            "additional": {"place": {"zone": 1, "cell": True}}})) == {"name/first": "One",
                                                                                      "name/last": "Drone",
                                                                                      "job": "scout", "recent": "",
                                                                                      "additional/place/zone": 1,
                                                                                      "additional/place/cell": True}


def test_multiple_values_empty():
    """Вводим пустой словарь"""
    assert (dicts.multiple_values({})) == 0


def test_multiple_values_with_different_type_of_values():
    """Вводим словарь со значениями разных типов"""
    assert (dicts.multiple_values({'a': 2, 'b': '2', 'c': True, 'd': -5})) == 0


def test_multiple_values_with_one_key():
    """Вводим словарь с одним ключом"""
    assert (dicts.multiple_values({'a': 5})) == 5


def test_multiple_values_with_two_keys():
    """Вводим словарь с двумя ключами"""
    assert (dicts.multiple_values({'a': 5, 'b': 7})) == 35


def test_multiple_values_with_negative_values():
    """Вводим словарь с отрицательными значениями"""
    assert (dicts.multiple_values({'a': -5, 'b': -7, 'c': -1})) == -35
