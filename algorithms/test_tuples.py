import pytest
from algorithms import tuples


def test_slicer_without_element():
    """Проверка кортежа и элемента, невходящего в этот кортеж"""

    assert (tuples.slicer((1, 2, 4, 5, 6, 7, 8, 4), 3)) == ()


def test_slicer_with_one_element():
    """Проверка с одним вхождением элемента в кортеж"""
    assert (tuples.slicer((1, 2, 4, 5, 6, 7, 3, 8, 4), 3)) == (3, 8, 4)


def test_slicer_with_two_elements():
    """Проверка с двумя вхождениями элементов в кортеж"""
    assert (tuples.slicer((1, 2, 3, 4, 5, 6, 7, 3, 8, 4), 3)) == (3, 4, 5, 6, 7, 3)


def test_slicer_with_three_elements():
    """Проверка с тремя вхождениями элементов в кортеж"""
    assert (tuples.slicer((1, 2, 3, 4, 5, 6, 7, 3, 8, 4, 3, 5, 6), 3)) == (3, 4, 5, 6, 7, 3)


def test_slicer_with_str_type():
    """Проверка кортежа с элементами строкового типа данных"""
    assert (tuples.slicer(('a', 'b', 'c', 'd', 'e', 'f', 'c', 'd', 'e'), 'c')) == ('c', 'd', 'e', 'f', 'c')


def test_slicer_with_diff_types():
    """Проверка кортежа с элементами разных типов данных"""
    assert (tuples.slicer(('a', 3, 'c', True, 4, 'f', 'c', 'd', 'e'), 'c')) == ('c', True, 4, 'f', 'c')


def test_sieve_unique_integers():
    """Проверка списка с уникальными целыми числами"""
    assert (tuples.sieve([1, 2, 4, 5, 6, 7, 8])) == (1, 2, 4, 5, 6, 7, 8)


def test_sieve_repeated_integers():
    """Проверка списка с повторяющимися целыми числами"""
    assert (tuples.sieve([1, 1, 2, 2, 0, 0, 4, 4, 3, 3])) == (0, 1, 2, 3, 4)


def test_sieve_diff_types_in_list():
    """Проверка списка с элементами разных типов"""
    with pytest.raises(TypeError):
        assert (tuples.sieve(['a', 3, 'c', True, 4, 'f', 'c', 'd', 'e']))


def test_sieve_other_type():
    """Проверка ввода иного типа данных"""
    with pytest.raises(TypeError):
        assert (tuples.sieve(4))


def test_sieve_float():
    """Проверка ввода списка с элементами типа чисел с плавающей точкой"""
    with pytest.raises(TypeError):
        assert (tuples.sieve([1.5, 1.4, 2.0, 2.7, 4.4, 4.3]))


def test_del_from_tuple_with_one_element():
    """Проверка ввода кортежа и одного элемента входящего в него"""
    assert (tuples.del_from_tuple((1, 2, 4, 5, 6, 7, 3, 8, 4), 3)) == (1, 2, 4, 5, 6, 7, 8, 4)


def test_del_from_tuple_with_two_elements():
    """Проверка ввода кортежа и двух элементов входящих в него"""
    assert (tuples.del_from_tuple((1, 2, 4, 3, 5, 6, 7, 3, 8, 4), 3)) == (1, 2, 4, 5, 6, 7, 3, 8, 4)


def test_del_from_tuple_without_element():
    """Проверка ввода кортежа и элемента невходящего в него"""
    assert (tuples.del_from_tuple((1, 2, 4, 5, 6, 7, 8, 4), 3)) == (1, 2, 4, 5, 6, 7, 8, 4)


def test_del_from_tuple_with_diff_types():
    """Проверка кортежа с элементами разных типов данных"""
    assert (tuples.del_from_tuple(('a', 3, 'c', True, 4, 'f', 'c', 'd', 'e'), 'c')) == (
        'a', 3, True, 4, 'f', 'c', 'd', 'e')
