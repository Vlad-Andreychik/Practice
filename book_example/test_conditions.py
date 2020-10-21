from book_example import conditions


# TODO[agorozhanko 16.10.2020]: тест падает
# TODO[vandreychyk 16.10.2020]: у меня он работает
def test_using_for():
    assert (conditions.using_for()) == 4
