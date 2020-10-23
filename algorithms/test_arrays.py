from algorithms import arrays


def test_max_even_elem_empty():
    """Проверка пустого ввода"""
    assert (arrays.max_even_elem([])) is None


def test_max_even_elem_diff_types():
    """Проверка ввода элементов разного типа"""
    assert (arrays.max_even_elem([3, True, 'a', 5])) is None


def test_max_even_elem_positive_numbers():
    """Проверка ввода положительных элементов"""
    assert (arrays.max_even_elem([1, 3, 23, 5, 43])) == 43


def test_max_even_elem_negative_numbers():
    """Проверка ввода отрицательных элементов"""
    assert (arrays.max_even_elem([-4, -7, -42, -3, -32])) == -4


def test_max_even_elem_one_element():
    """Проверка ввода одного элемента"""
    assert (arrays.max_even_elem([5])) == 5


def test_max_even_elem_equal_numbers():
    """Проверка ввода одинаковых элементов"""
    assert (arrays.max_even_elem([5, 5, 5, 5, 5, 5, 5])) == 5


def test_swap_max_and_min_empty():
    """Проверка пустого ввода"""
    assert (arrays.swap_max_and_min([])) is None


def test_swap_max_and_min_one_element():
    """Проверка ввода одного элемента"""
    assert (arrays.swap_max_and_min([5])) == [5]


def test_swap_max_and_min_diff_types():
    """Проверка ввода элементов разного типа"""
    assert (arrays.swap_max_and_min([5, False, 'b'])) is None


def test_swap_max_and_min_equal_numbers():
    """Проверка ввода одинаковых элементов"""
    assert (arrays.swap_max_and_min([5, 5, 5, 5])) == [5, 5, 5, 5]


def test_swap_max_and_min_several_min_and_max_numbers():
    """Проверка ввода нескольких элементов с минимальным и максимальным значениями"""
    assert (arrays.swap_max_and_min([5, 7, 1, 65, 34, 65, 1])) == [5, 7, 65, 1, 34, 65, 1]


def test_swap_max_and_min_border_positions():
    """Проверка ввода минимального и максимального элементов на гравницах массива"""
    assert (arrays.swap_max_and_min([1, 70, 11, 32, 34, 65, 90])) == [90, 70, 11, 32, 34, 65, 1]


def test_delete_negatives_one_negative():
    """Проверка одного отрицательного числа"""
    assert (arrays.delete_negatives([-3])) == []


def test_delete_negatives_positive_and_negative_numbers():
    """Проверка ввода положительных и отрицательных элементов"""
    assert (arrays.delete_negatives([5, -8, -9, 40, 1, 5])) == [5, 40, 1, 5]


def test_delete_negatives_only_negatives():
    """Проверка ввода только отрицательных чисел"""
    assert (arrays.delete_negatives([-3, -1, -7, -32])) == []


def test_delete_negatives_only_positives():
    """Проверка ввода только отрицательных чисел"""
    assert (arrays.delete_negatives([3, 1, 7, 32])) == [3, 1, 7, 32]


def test_selection_sort_equal_numbers():
    """Проверка ввода одинаковых элементов"""
    assert (arrays.selection_sort([5, 5, 5, 5])) == [5, 5, 5, 5]


def test_selection_sort_normal_input():
    """Проверка нормального ввода"""
    assert (arrays.selection_sort([1, 70, 11, 32, 34, 65, 90])) == [1, 11, 32, 34, 65, 70, 90]


def test_selection_sort_repeated_numbers():
    """Проверка ввода повторяющихся чисел"""
    assert (arrays.selection_sort([1, 70, 11, 32, 1, 11, 11])) == [1, 1, 11, 11, 11, 32, 70]


def test_frequency_sorting_unique_numbers():
    """Проверка ввода уникальных значений"""
    assert (arrays.frequency_sorting([1, 70, 11, 32, 34, 65, 90])) == [1, 11, 32, 34, 65, 70, 90]


def test_frequency_sorting_repeated_numbers():
    """Проверка ввода повторяющихся чисел"""
    assert (arrays.frequency_sorting([1, 70, 11, 32, 1, 11, 11])) == [11, 11, 11, 1, 1, 32, 70]


def test_frequency_sorting_one_repeated_number():
    """Проверка ввода одного повторяющегося числа"""
    assert (arrays.frequency_sorting([1, 1, 1, 1, 1, 1])) == [1, 1, 1, 1, 1, 1]


def test_frequency_sorting_same_modules():
    """Проверка ввода одинаковых по модулю, но разных по знаку чисел"""
    assert (arrays.frequency_sorting([1, -1, 5, -5, 47, -20, 1, -5, -5])) == [-5, -5, -5, 1, 1, -20, -1, 5, 47]
