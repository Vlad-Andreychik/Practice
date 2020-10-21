from data_examples import strings


# TODO[agorozhanko 21.10.2020]: что будет если ввести непроинициализированую строку (это относится ко всем тестам)?
# TODO[agorozhanko 21.10.2020]: что будет если ввести спец символы (это относится ко всем тестам)?
# TODO[agorozhanko 21.10.2020]: что будет если ввести строку состоящую только из пробелов (это относится ко всем тестам)?


def test_reverse_word():
    """Проверка слова"""
    assert (strings.reverse('text')) == 'txet'


def test_reverse_numbers():
    """Проверка на наборе цифр"""
    assert (strings.reverse('5427890')) == '0987245'


def test_reverse_sentence():
    """Проверка на предложении"""
    assert (strings.reverse('Hello world')) == 'dlrow olleH'


def test_unrepeated_letters_in_word():
    """Проверка слова"""
    assert (strings.unrepeated_letters('letter')) == 'letr'


def test_unrepeated_letters_in_numbers():
    """Проверка на наборе цифр"""
    assert (strings.unrepeated_letters('45454545')) == '45'


def test_unrepeated_letters_in_sentence():
    """Проверка на предложении"""
    assert (strings.unrepeated_letters('Hello world')) == 'Helowrd'


def test_count_words_empty_string():
    """Проверка пустой строки"""
    assert (strings.count_words('')) == 0


# TODO[agorozhanko 21.10.2020]: что будет если ввести строку с лишними пробелами в всех частях предложения
def test_count_words_sentence_without_numbers():
    """Проверка предложения"""
    assert (strings.count_words('Hello world')) == 2


def test_count_words_sentence_with_numbers():
    """Проверка предложения с числами"""
    assert (strings.count_words('5 apples')) == 2


def test_change_piece_empty_new_piece():
    """Проверка с пустым новым куском"""
    assert (strings.change_piece('application', 'ion', '')) == 'applicat'


def test_change_piece_not_existing_old_piece():
    """Проверка с несуществующим заменямым куском"""
    assert (strings.change_piece('application', 'h', 'tok')) == 'applicatiotok'


def test_change_piece_normal_input():
    # TODO[agorozhanko 21.10.2020]: опечатка
    """Проверка с существующим заменямым куском"""
    assert (strings.change_piece('application', 'appli', 'californi')) == 'californication'


# TODO[agorozhanko 21.10.2020]: что будет если ввести отрицательные числа или 0
def test_sum_numbers_digits_only():
    """Проверка строки только из цифр"""
    assert (strings.sum_numbers('45')) == 9


def test_sum_numbers_without_digits():
    """Проверка строки без цифр"""
    assert (strings.sum_numbers('asdf')) == 0


def test_sum_numbers_letters_and_digits():
    """Проверка строки с цифрами и буквами"""
    assert (strings.sum_numbers('as3df5  7')) == 15


def test_reverse_words_positions_one_word():
    """Проверка строки с одним словом"""
    assert (strings.reverse_words_positions('word')) == 'word'


# TODO[agorozhanko 21.10.2020]: что будет если ввести строку с лишними пробелами в всех частях предложения
def test_reverse_words_positions_sentence():
    """Проверка на предложении"""
    assert (strings.reverse_words_positions('Hello world')) == 'world Hello'


def test_reverse_words_positions_empty():
    """Проверка пустой строки"""
    assert (strings.reverse_words_positions('')) == ''


def test_delete_spaces_in_the_start():
    """Проверка строки с пробелами в начале"""
    assert (strings.delete_spaces('    word')) == 'word'


def test_delete_spaces_in_the_end():
    """Проверка строки с пробелами в конце"""
    assert (strings.delete_spaces('word    ')) == 'word'


def test_delete_spaces_everywhere():
    """Проверка строки с пробелами в начале, в конце и между слов"""
    assert (strings.delete_spaces('   Hello   world     ')) == 'Hello world'
