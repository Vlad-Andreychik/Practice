from book_example import modules


def test_imp_sys():
    # TODO[agorozhanko 14.10.2020]:при запуске функции на другом компьютере, проверка не пройдёт
    # TODO[vandreychyk 15.10.2020]:удалил эту проверку
    # TODO[agorozhanko 16.10.2020]:проблемы в плохом коде нужно решать хорошим кодом а не его удалением
    # TODO[agorozhanko 16.10.2020]:тест всё равно падает
    assert (len(modules.imp_sys())) == 2


def test_simple_or_not():
    assert (modules.simple_or_not(5)) == [2, 3, 5, 7]
    assert (modules.simple_or_not(-5)) == [2, 3]


def test_using_name():
    assert (modules.using_name()) == 'modules'


def test_say_hi():
    assert (modules.say_hi()) == 'Привет! Это говорит мой модуль.'
