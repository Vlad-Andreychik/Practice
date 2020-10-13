import modules


def test_imp_sys():
    a = modules.imp_sys()
    assert (a[0]) == 'C:\\Users\\vandreychyk\\PycharmProjects\\Practice'
    assert (len(a)) == 7
