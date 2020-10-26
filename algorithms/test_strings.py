import logging

import pytest
from algorithms import strings

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('..//logs//string.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# TODO[agorozhanko 21.10.2020]: что будет если ввести непроинициализированую строку (это относится ко всем тестам)?
# TODO[vandreychyk 21.10.2020]: сделал все эти проверки ко всем примерам
# TODO[agorozhanko 22.10.2020]: не все проверки сделал

a = None


def test_reverse_word():
    """Проверка слова"""
    assert (strings.reverse('text')) == 'txet'


def test_reverse_uninitialized_string():
    """Проверка непроинициализированой строки"""
    with pytest.raises(Exception):
        strings.reverse(a)


def test_reverse_special_symbols():
    """Проверка специальных символов"""
    assert (strings.reverse('%$(/*-!')) == '!-*/($%'


def test_reverse_only_spaces():
    """Проверка строки состоящей только из пробелов"""
    assert (strings.reverse('     ')) == '     '


def test_reverse_numbers():
    """Проверка на наборе цифр"""
    assert (strings.reverse('5427890')) == '0987245'


def test_reverse_sentence():
    """Проверка на предложении"""
    assert (strings.reverse('Hello world')) == 'dlrow olleH'


def test_unrepeated_letters_in_word():
    """Проверка слова"""
    assert (strings.unrepeated_letters('letter')) == 'letr'


def test_unrepeated_letters_special_symbols():
    """Проверка специальных символов"""
    assert (strings.unrepeated_letters('///@@@!!!$$$%%%')) == '/@!$%'


def test_unrepeated_letters_uninitialized_string():
    """Проверка непроинициализированой строки"""
    with pytest.raises(Exception):
        strings.unrepeated_letters(a)


def test_unrepeated_letters_only_spaces():
    """Проверка строки состоящей только из пробелов"""
    assert (strings.unrepeated_letters('     ')) == ''


def test_unrepeated_letters_in_numbers():
    """Проверка на наборе цифр"""
    assert (strings.unrepeated_letters('45454545')) == '45'


def test_unrepeated_letters_in_sentence():
    """Проверка на предложении"""
    assert (strings.unrepeated_letters('Hello world')) == 'Helowrd'


def test_count_words_empty_string():
    """Проверка пустой строки"""
    assert (strings.count_words('')) == 0


def test_count_words_uninitialized_string():
    """Проверка непроинициализированой строки"""
    with pytest.raises(Exception):
        strings.count_words(a)


# TODO[agorozhanko 22.10.2020]: являются ли спецсимволы, в частности знаки препинания словами?
# TODO[vandreychyk 22.10.2020]: добавил в функцию проверку на спецсимволы
def test_count_words_special_symbols():
    """Проверка специальных символов"""
    assert (strings.count_words('%$(/*-!')) == 1


def test_count_words_only_spaces():
    """Проверка строки состоящей только из пробелов"""
    assert (strings.count_words('     ')) == 0


def test_count_words_unnecessary_spaces():
    """Проверка строки с лишними пробелами"""
    assert (strings.count_words('    Hello    world    ')) == 2


def test_count_words_sentence_without_numbers():
    """Проверка предложения"""
    assert (strings.count_words('Hello world')) == 2


def test_count_words_sentence_with_numbers():
    """Проверка предложения с числами"""
    assert (strings.count_words('5 apples')) == 2


def test_change_piece_empty_new_piece():
    """Проверка с пустым новым куском"""
    assert (strings.change_piece('application', 'ion', '')) == 'applicat'


def test_change_piece_uninitialized_string():
    """Проверка непроинициализированой строки"""
    with pytest.raises(Exception):
        strings.change_piece(a)


def test_change_piece_special_symbols():
    """Проверка специальных символов"""
    assert (strings.change_piece('%$(/*-!', 'h', 'tok')) == '%$(/*-tok'


def test_change_piece_only_spaces():
    """Проверка строки состоящей только из пробелов"""
    assert (strings.change_piece('     ', 'h', 'tok')) == '    tok'


def test_change_piece_not_existing_old_piece():
    """Проверка с несуществующим заменяемым куском"""
    assert (strings.change_piece('application', 'h', 'tok')) == 'applicatiotok'


def test_change_piece_normal_input():
    """Проверка с существующим заменяемым куском"""
    assert (strings.change_piece('application', 'appli', 'californi')) == 'californication'


def test_sum_numbers_negative_numbers():
    """Проверка на отрицательные числа"""
    assert (strings.sum_numbers('-5-7-8')) == -20


def test_sum_numbers_nulls():
    """Проверка нулей"""
    assert (strings.sum_numbers('000000')) == 0


def test_sum_numbers_digits_only():
    """Проверка строки только из цифр"""
    assert (strings.sum_numbers('45')) == 9


def test_sum_numbers_uninitialized_string():
    """Проверка непроинициализированой строки"""
    with pytest.raises(Exception):
        strings.sum_numbers(a)


def test_sum_numbers_special_symbols():
    """Проверка специальных символов"""
    assert (strings.sum_numbers('%$(/*-!')) == 0


def test_sum_numbers_only_spaces():
    """Проверка строки состоящей только из пробелов"""
    assert (strings.sum_numbers('     ')) == 0


def test_sum_numbers_without_digits():
    """Проверка строки без цифр"""
    assert (strings.sum_numbers('asdf')) == 0


def test_sum_numbers_letters_and_digits():
    """Проверка строки с цифрами и буквами"""
    assert (strings.sum_numbers('as3df5  7')) == 15


def test_reverse_words_positions_one_word():
    """Проверка строки с одним словом"""
    assert (strings.reverse_words_positions('word')) == 'word'


def test_reverse_words_positions_uninitialized_string():
    """Проверка непроинициализированой строки"""
    with pytest.raises(Exception):
        strings.reverse_words_positions(a)


def test_reverse_words_positions_special_symbols():
    """Проверка специальных символов"""
    assert (strings.reverse_words_positions('%$(/*-!')) == '%$(/*-!'


def test_reverse_words_positions_only_spaces():
    """Проверка строки состоящей только из пробелов"""
    assert (strings.reverse_words_positions('     ')) == ''


def test_reverse_words_positions_sentence_with_unnecessary_spaces():
    """Проверка на предложении с лишними пробелами в всех частях предложения"""
    assert (strings.reverse_words_positions('   Hello   world   ')) == 'world Hello'


def test_reverse_words_positions_sentence():
    """Проверка на предложении"""
    assert (strings.reverse_words_positions('Hello world')) == 'world Hello'


def test_reverse_words_positions_empty():
    """Проверка пустой строки"""
    assert (strings.reverse_words_positions('')) == ''


def test_delete_spaces_in_the_start():
    """Проверка строки с пробелами в начале"""
    assert (strings.delete_spaces('    word')) == 'word'


def test_delete_spaces_uninitialized_string():
    """Проверка непроинициализированой строки"""
    with pytest.raises(Exception):
        strings.delete_spaces(a)


def test_delete_spaces_special_symbols():
    """Проверка специальных символов"""
    assert (strings.delete_spaces('%$(/*-!')) == '%$(/*-!'


def test_delete_spaces_only_spaces():
    """Проверка строки состоящей только из пробелов"""
    assert (strings.delete_spaces('     ')) == ''


def test_delete_spaces_in_the_end():
    """Проверка строки с пробелами в конце"""
    assert (strings.delete_spaces('word    ')) == 'word'


def test_delete_spaces_everywhere():
    """Проверка строки с пробелами в начале, в конце и между слов"""
    assert (strings.delete_spaces('   Hello   world     ')) == 'Hello world'
