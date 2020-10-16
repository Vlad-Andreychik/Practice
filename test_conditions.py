import conditions


def test_using_while():
    a = conditions.using_while()
    assert (a()[0]) is False
    assert (a()[1]) == 6


# TODO[agorozhanko 16.10.2020]: тест падает
def test_using_for():
    assert (conditions.using_for()) == 4
