import structures


def test_shop():
    assert (structures.shop()) == ['манго', 'морковь', 'рис', 'яблоки']
    assert (len(structures.shop())) == 4


def test_using_tuple():
    assert (structures.using_tuple()) == ('обезьяна', 'верблюд', ('питон', 'слон', 'пингвин'))
    assert (structures.using_tuple()[0:2]) == ('обезьяна', 'верблюд')
