from book_example import structures


def test_shop():
    assert (structures.shop()) == ['манго', 'морковь', 'рис', 'яблоки']
    assert (len(structures.shop())) == 4


def test_using_tuple():
    assert (structures.using_tuple()) == ('обезьяна', 'верблюд', ('питон', 'слон', 'пингвин'))
    assert (structures.using_tuple()[0:2]) == ('обезьяна', 'верблюд')


def test_using_dict():
    assert (len(structures.using_dict())) == 4
    assert (structures.using_dict()['Matsumoto']) == 'matz@ruby-lang.org'


def test_seq():
    assert (structures.seq()[-1]) == 'бананы'
    assert (len(structures.seq())) == 4


def test_reference():
    assert (len(structures.reference()[0]) - len(structures.reference()[1])) == -1


def test_str_methods():
    assert (structures.str_methods()[0].startswith('Swa'))
    assert ('Россия' in structures.str_methods()[1])
