import modules


def test_imp_sys():
    a = modules.imp_sys()
    # TODO[agorozhanko 14.10.2020]:при запуске функции на другом компьютере, проверка не пройдёт
    # TODO[vandreychyk 15.10.2020]:удалил эту проверку
    assert (len(a)) == 7


def test_simple_or_not():
    assert (modules.simple_or_not(5)) == [2, 3, 5, 7]
    assert (modules.simple_or_not(-5)) == [2, 3]


def test_using_name():
    assert (modules.using_name()) == 'modules'


# TODO[agorozhanko 14.10.2020]: название нужно исправить
# TODO[vandreychyk 15.10.2020]: название исправлено
def test_say_hi():
    assert (modules.sayhi()) == 'Привет! Это говорит мой модуль.'
