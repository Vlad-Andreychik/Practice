from data_examples import dicts


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
