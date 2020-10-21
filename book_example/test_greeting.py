from book_example import greeting


def test_greeting():
    assert (greeting.greeting()[0]) == 6
    assert (len(greeting.greeting())) == 4
