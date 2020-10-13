import modules


def test_imp_sys():
    a = modules.imp_sys()
    assert (a[0]) == 'C:\\Users\\vandreychyk\\PycharmProjects\\Practice'
    assert (len(a)) == 7


def test_simple_or_not():
    assert (modules.simple_or_not(5)) == [2, 3, 5, 7]
    assert (modules.simple_or_not(-5)) == [2, 3]


def test_using_name():
    assert (modules.using_name()) == 'modules'


def test_sayhi():
    assert (modules.sayhi()) == 'Привет! Это говорит мой модуль.'
