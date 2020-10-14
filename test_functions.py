import functions


def test_say_hello():
    assert (type(functions.sayHello())) == str
    assert (functions.sayHello()) == 'Привет, Мир!'


# TODO[agorozhanko 14.10.2020]: название нужно исправить
def test_printmax():
    assert (functions.printMax(7, 8)) == 8
    assert (functions.printMax(8, 8)) == 8
    assert (functions.printMax(9, 8)) == 9


def test_unc():
    assert (functions.func(10)) == (10, 2)
    assert (functions.func_global()) == (105, 2)
    assert (functions.func_outer()) == (2, 5)


def test_say():
    assert (functions.say('message', 3)) == ('message', 3, 'messagemessagemessage')


def test_key():
    assert (functions.func_key(1)) == (1, 5, 10)
    assert (functions.func_key(1, 2)) == (1, 2, 10)
    assert (functions.func_key(1, 2, 3)) == (1, 2, 3)
    assert (functions.func_key(1, c=7)) == (1, 5, 7)
    assert (functions.func_key(1, b=105)) == (1, 105, 10)
    assert (functions.func_key(1, c=2, b=3)) == (1, 3, 2)


def test_total():
    # TODO[agorozhanko 14.10.2020]: название нужно исправить
    phonebook = {'jerry': 123, 'kok': 432}
    assert (functions.total(3, 5, 7, jerry=123, kok=432)) == (3, [5, 7], phonebook)


def test_keyword_only():
    assert (functions.total_only(1, 54, 8, 6)) == 70
    assert (functions.total_only(5, 5, extra_number=5)) == 15


def test_maximum():
    assert (functions.printMax(7, 8)) == 8
    assert (functions.printMax(8, 8)) == 8
    assert (functions.printMax(9, 8)) == 9


def test_desc():
    assert (type(functions.printMax_desc.__doc__)) == str
