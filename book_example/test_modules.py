import os

from book_example import module


def test_imp_sys():
    # TODO[agorozhanko 14.10.2020]:при запуске функции на другом компьютере, проверка не пройдёт
    # TODO[vandreychyk 15.10.2020]:удалил эту проверку
    # TODO[agorozhanko 16.10.2020]:проблемы в плохом коде нужно решать хорошим кодом а не его удалением
    # TODO[agorozhanko 21.10.2020]: когда замечания выше будут исправлены?
    cur_dir = os.path.abspath(os.curdir)
    assert cur_dir in module.imp_sys()[1]
    assert (len(module.imp_sys()[0])) != 0


def test_simple_or_not():
    assert (module.simple_or_not(5)) == [2, 3, 5, 7]
    assert (module.simple_or_not(-5)) == [2, 3]


# TODO[agorozhanko 21.10.2020]: тест падает
# TODO[vandreychyk 21.10.2020]: должен нормально заработать как только я правильно venv настрою
def test_using_name():
    assert (module.using_name()) == 'modules'


def test_say_hi():
    assert (module.say_hi()) == 'Привет! Это говорит мой модуль.'
