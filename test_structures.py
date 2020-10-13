import structures


def test_shop():
    assert (structures.shop()) == ['манго', 'морковь', 'рис', 'яблоки']
    assert (len(structures.shop())) == 4
