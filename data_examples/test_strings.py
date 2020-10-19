import strings


def test_reverse_word():
    assert (strings.reverse('text')) == 'txet'


def test_reverse_numbers():
    assert (strings.reverse('5427890')) == '0987245'


def test_reverse_sentence():
    assert (strings.reverse('Hello world')) == 'dlrow olleH'


def test_unrepeated_letters_in_word():
    assert (strings.unrepeated_letters('letter')) == 'letr'


def test_unrepeated_letters_in_numbers():
    assert (strings.unrepeated_letters('45454545')) == '45'


def test_unrepeated_letters_in_sentence():
    assert (strings.unrepeated_letters('Hello world')) == 'Helowrd'


def test_count_words_empty_string():
    assert (strings.count_words('')) == 0


def test_count_words_sentence_without_numbers():
    assert (strings.count_words('Hello world')) == 2


def test_count_words_sentence_with_numbers():
    assert (strings.count_words('5 apples')) == 2


def test_change_piece_empty_new_piece():
    assert (strings.change_piece('application', 'ion', '')) == 'applicat'


def test_change_piece_empty_old_piece():
    assert (strings.change_piece('application', 'h', 'tok')) == 'applicatiotokapplication'


def test_change_piece_normal_input():
    assert (strings.change_piece('application', 'appli', 'californi')) == 'californication'
