import modules


# TODO[agorozhanko 14.10.2020]: это не тесты а просто функции которые не запускаются, для написания тестов нужно
#  использовать библитотеку pytest
def test_imp_sys():
    a = modules.imp_sys()
    # TODO[agorozhanko 14.10.2020]:при запуске функции на другом компьютере, проверка не пройдёт
    assert (a[0]) == 'C:\\Users\\vandreychyk\\PycharmProjects\\Practice'
    assert (len(a)) == 7


def test_simple_or_not():
    assert (modules.simple_or_not(5)) == [2, 3, 5, 7]
    assert (modules.simple_or_not(-5)) == [2, 3]


def test_using_name():
    assert (modules.using_name()) == 'modules'


# TODO[agorozhanko 14.10.2020]: название нужно исправить
def test_sayhi():
    assert (modules.sayhi()) == 'Привет! Это говорит мой модуль.'
