import os

from book_example import module


def test_imp_sys():
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
